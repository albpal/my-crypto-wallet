import ecdsa
import hashlib
import base58
import secrets
import binascii

class AddressFormat:
    def __init__(self, format):
        if format.lower() == "segwit":
            raise("Function to be done.")
        elif format.lower() == "classic":
            self.format_func = self.classic
        else:
            raise BaseException("Error: Address format %s is not valid."%(format))

    def format(self, address):
        return self.format_func(address)

    def classic(self, address):
        return address

class PublicKeyFormat:
    def __init__(self, format):
        if format.lower() == "compress":
            raise("Function to be done.")
        elif format.lower() == "uncompress":
            self.format_func = self.uncompressFormat
        else:
            raise BaseException("Error: Public key format %s is not valid."%(format))

    def format(self, pubKey):
        return self.format_func(pubKey)

    def uncompressFormat(self, pubKey):
        return pubKey

class PrivateKeyFormat:
    def __init__(self, format):
        if format.upper() == "WIF":
            raise("Function to be done.")
        elif format.upper() == "STANDARD":
            self.format_func = self.standardFormat
        else:
            raise BaseException("Error: Private key format %s is not valid."%(format))

    def format(self, privKey):
        return self.format_func(privKey)

    def standardFormat(self, privKey):
        return privKey

class Address:
    ## This Address class stores its data in big endian bytes
    ##      self.privKey is in its standard format (raw number stored in bytes)
    ##      The rest of the data are generated on the fly depending of the different configurations (mainly formats)
    ## Useful link: https://en.bitcoin.it/wiki/Address, https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
    def __init__(self, privKeyFormat="standard", pubKeyFormat="uncompress", addressFormat="classic", privKey=None):
        self.privKeyFormat = PrivateKeyFormat(privKeyFormat)
        self.pubKeyFormat = PublicKeyFormat(pubKeyFormat)
        self.addressFormat = AddressFormat(addressFormat)
        if privKey is None:
            self.privKey = None # Instantiate instance variable
            self.privKey = self.generatePrivateKey()
        else:
            self.privKey = privKey

    def getPrivKey(self):
        return self.privKeyFormat.format(self.privKey)

    def getPubKey(self):
        pubKey = self.generatePublicKey(self.privKey)
        return self.pubKeyFormat.format(pubKey)

    def getAddress(self):
        btc_addr = self.generateAddress(self.getPubKey())
        return self.addressFormat.format(btc_addr)

    def generateAddress(self, pubKey):
        pubKeySHA256 = hashlib.sha256(self.getPubKey()).digest()
        hash160 = self.ripemd160(pubKeySHA256).digest()
        addr_without_checksum = binascii.unhexlify("00") + hash160
        checksum = hashlib.sha256(hashlib.sha256(addr_without_checksum).digest()).digest()[:4]
        btc_addr = base58.b58encode(addr_without_checksum + checksum)
        return btc_addr

    def generatePublicKey(self, privKey):
        return binascii.unhexlify("04") + bytes(ecdsa.SigningKey.from_string(privKey, curve=ecdsa.SECP256k1).get_verifying_key().to_string())

    def generatePrivateKey(self):
        if self.privKey is not None:
            return self.privKey
        number = int(secrets.randbelow(1 << 256))
        while number == 0 or number > 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140:
            number = secrets.randbelow(1 << 256)
        return number.to_bytes(32, byteorder='big')

    def ripemd160(self, x):
        d = hashlib.new('ripemd160')
        d.update(x)
        return d

    def sign(self, data):
        return b"to be done"
