import ecdsa
import hashlib
import base58
import secrets
import binascii
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from formats import *
from utils import *

class Address:
    ## This Address class stores its data in big endian bytes
    ##      self.privKey is in its standard format (raw number stored in bytes)
    ##      The rest of the data are generated on the fly depending of the different configurations (mainly formats)
    ## Useful links: 
    #   - https://en.bitcoin.it/wiki/Address
    #   - https://bitcoin.org/en/developer-guide#private-key-formats
    #   - https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
    def __init__(self, privKey=None):
        if privKey is None:
            self.privKey = None # Instantiate instance variable
            self.privKey = self.generatePrivateKey()
        else:
            if len(privKey) < 64:
                if privKey[0] == "5": # WIF format uncompressed
                    self.privKey = base58.b58decode(privKey)[1:-4]
                elif privKey[0] == "L" or privKey[0] == "K": # WIF format compressed
                    self.privKey = base58.b58decode(privKey)[1:-5]
                else:
                    raise BaseException("Incorrect private key %s"%(privKey))
            else:
                self.privKey = binascii.unhexlify(privKey)

    def getPrivKey(self, format="standard"):
        return PrivateKeyFormat(format).format(self.privKey)

    def getPubKey(self, format="uncompressed"):
        pubKey = self.generatePublicKey(self.privKey)
        return PublicKeyFormat(format).format(pubKey)

    def getAddress(self, format="classic"):
        return AddressFormat(format).format(self.generatePublicKey(self.privKey))

    def generatePublicKey(self, privKey):
        return bytes(ecdsa.SigningKey.from_string(privKey, curve=ecdsa.SECP256k1).get_verifying_key().to_string())

    def generatePrivateKey(self):
        if self.privKey is not None:
            return self.privKey
        number = int(secrets.randbelow(1 << 256))
        while number == 0 or number > 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140:
            number = secrets.randbelow(1 << 256)
        return number.to_bytes(32, byteorder='big')

    def sign(self, data):
        sk = ecdsa.SigningKey.from_string(self.privKey, curve=ecdsa.SECP256k1)
        return sk.sign(data)

    def verify(self, data, signature):
        vk = ecdsa.SigningKey.from_string(self.privKey, curve=ecdsa.SECP256k1).get_verifying_key()
        try:
            return vk.verify(signature, data)
        except ecdsa.keys.BadSignatureError:
            return False
        except:
            raise BaseException("Verify failed. Unhandled exception.")

