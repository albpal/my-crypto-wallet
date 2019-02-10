import ecdsa
import binascii
import hashlib
import base58
import sys
import os
import secrets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from utils import *


class PublicKey:
    def __init__(self, privKey):
        self.pubKey = binascii.hexlify(self.generatePublicKey(privKey))

    def generatePublicKey(self, privKey):
        bytes_privKey = binascii.unhexlify(privKey.get())
        return ecdsa.SigningKey.from_string(bytes_privKey, curve=ecdsa.SECP256k1).get_verifying_key().to_string()

    def get(self, format="UNCOMPRESSED"):
        if format.upper() == "COMPRESSED":
            return self.compressedFormat()
        elif format.upper() == "UNCOMPRESSED":
            return self.uncompressedFormat()
        elif format.upper() == "RAW-HEX":
            return self.raw_hex()
        else:
            raise BaseException("Error: PublicKey format %s is not valid."%(format))

    def raw_hex(self):
        return self.pubKey

    def uncompressedFormat(self):
        return binascii.hexlify(binascii.unhexlify("04") + binascii.unhexlify(self.pubKey)).decode()

    def compressedFormat(self):
        x = self.pubKey[:64]
        y = self.pubKey[64:]
        if int(y,base=16) % 2 == 0:
            prefix = "02"
        else:
            prefix = "03"
        return binascii.hexlify(binascii.unhexlify(prefix) + binascii.unhexlify(x)).decode()
