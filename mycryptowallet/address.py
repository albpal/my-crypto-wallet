import ecdsa
import hashlib
import base58
import secrets
import binascii
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from bitcoinAddress import *
from utils import *
from privateKey import *
from publicKey import * 

class Address:
    ## This Address class stores its data in big endian bytes
    ##      self.privKey is in its standard format (raw number stored in bytes)
    ##      The rest of the data are generated on the fly depending of the different configurations (mainly formats)
    ## Useful links: 
    #   - https://en.bitcoin.it/wiki/Address
    #   - https://bitcoin.org/en/developer-guide#private-key-formats
    #   - https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
    def __init__(self, privKey=None, n=1, m=1):
        self.privKey = PrivateKey(privKey=privKey)
        self.pubKey = PublicKey(self.privKey)
        self.bitcoin_address = BitcoinAddress(self.pubKey, n=n, m=m)

    def multisig(self, pubKeys, n=1, m=1):
        self.bitcoin_address = BitcoinAddress(pubKeys, n=n, m=m)

    def getPrivKey(self, format="RAW-HEXA"):
        return self.privKey.get(format)

    def getPubKey(self, format="uncompressed"):
        return self.pubKey.get(format=format)

    def getAddress(self, format="p2pkh"):
        return self.bitcoin_address.get(format)

    def sign(self, data):
        bytes_privKey = binascii.unhexlify(self.privKey.get())
        sk = ecdsa.SigningKey.from_string(bytes_privKey, curve=ecdsa.SECP256k1)
        return sk.sign(data)

    def verify(self, data, signature):
        bytes_privKey = binascii.unhexlify(self.privKey.get())
        vk = ecdsa.SigningKey.from_string(bytes_privKey, curve=ecdsa.SECP256k1).get_verifying_key()
        try:
            return vk.verify(signature, data)
        except ecdsa.keys.BadSignatureError:
            return False
        except:
            raise BaseException("Verify failed. Unhandled exception.")

