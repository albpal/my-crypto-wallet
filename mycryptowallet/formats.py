import binascii
import hashlib
import base58

class Format:
    def __init__(self, format):
        if format.lower() == "segwit":
            raise("Function to be done.")
        elif format.lower() == "classic":
            self.format_func = AddressFormat.classic
        elif format.lower() == "compressed":
            self.format_func = PublicKeyFormat.compressedFormat
        elif format.lower() == "uncompress":
            self.format_func = PublicKeyFormat.uncompressedFormat
        elif format.upper() == "WIF-UNCOMPRESSED":
            self.format_func = PrivateKeyFormat.WIFUncompressedFormat
        elif format.upper() == "WIF-COMPRESSED":
            self.format_func = PrivateKeyFormat.WIFCompressedFormat
        elif format.upper() == "STANDARD":
            self.format_func = PrivateKeyFormat.standardFormat
        else:
            raise BaseException("Error: format %s is not valid."%(format))

    def format(self, object):
        return self.format_func(object)

class AddressFormat:
    def classic(address):
        return address

class PublicKeyFormat:
    def uncompressedFormat(pubKey):
        return pubKey

    def compressedFormat(pubKey):
        x = binascii.hexlify(pubKey)[2:][:64]
        y = binascii.hexlify(pubKey)[2:][64:]
        if int(y,base=16) % 2 == 0:
            prefix = binascii.unhexlify("02")
        else:
            prefix = binascii.unhexlify("03")
        return base58.b58encode(prefix + binascii.unhexlify(x))

class PrivateKeyFormat:
    def standardFormat(privKey):
        return privKey
    
    def WIFUncompressedFormat(privKey):
        mainnet_address = binascii.unhexlify("80") + privKey
        checksum = hashlib.sha256(hashlib.sha256(mainnet_address).digest()).digest()[:4]
        return base58.b58encode(mainnet_address + checksum)

    def WIFCompressedFormat(privKey):
        mainnet_address = binascii.unhexlify("80") + privKey + binascii.unhexlify("01")
        checksum = hashlib.sha256(hashlib.sha256(mainnet_address).digest()).digest()[:4]
        return base58.b58encode(mainnet_address + checksum)
