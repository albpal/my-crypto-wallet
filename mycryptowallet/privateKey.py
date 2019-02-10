import binascii
import hashlib
import base58
import sys
import os
import secrets
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from utils import *

class PrivateKey:
    def __init__(self, privKey=None, net="main"):
        if privKey == None:
            privKey = self.generatePrivateKey()
        if not self.isValid(privKey):
            raise BaseException("Incorrect private key %s"%(privKey))
        self.privKey = self.parse(privKey)
        self.netCode = self.getNetID(net)

    def isValid(self, privKey):
        return self.isWIFUncompressed(privKey) or self.isWIFCompressed(privKey) or self.isRawHexa(privKey)

    def isWIFUncompressed(self, privKey):
        return privKey[0] == "5" 

    def isWIFCompressed(self, privKey):
        return privKey[0] == "L" or privKey[0] == "K"

    def isRawHexa(self, privKey):
        if len(privKey) != 64:
            return False
        int_privKey = int(privKey, 16)
        return int_privKey > 0 and int_privKey <= int("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140", 16)

    def parse(self, privKey):
        if self.isWIFUncompressed(privKey):
            return binascii.hexlify(base58.b58decode(privKey)[1:-4])
        if self.isWIFCompressed(privKey):
            return binascii.hexlify(base58.b58decode(privKey)[1:-5])
        if self.isRawHexa(privKey):
            return privKey
        raise BaseException("Incorrect private key %s"%(privKey))

    def getNetID(self, long_format):
        if long_format == "main":
            return "80"
        else:
            raise BaseException("Incorrect network identifier %s"%(long_format))

    def get(self, format="RAW-HEXA"):
        if format.upper() == "WIF-UNCOMPRESSED":
            return self.WIFUncompressedFormat()
        elif format.upper() == "WIF-COMPRESSED":
            return self.WIFCompressedFormat()
        elif format.upper() == "RAW-HEXA":
            return self.rawHexaFormat()
        else:
            raise BaseException("Error: PrivateKey format %s is not valid."%(format))

    def rawHexaFormat(self):
        return self.privKey

    def WIFUncompressedFormat(self):
        formated_privKey = binascii.unhexlify(self.netCode) + binascii.unhexlify(self.privKey)
        checksum = doubleSHA256(formated_privKey).digest()[:4]
        return formated_privKey + checksum

    def WIFCompressedFormat(self):
        formated_privKey = binascii.unhexlify(self.netCode) + binascii.unhexlify(self.privKey) + binascii.unhexlify("01")
        checksum = doubleSHA256(formated_privKey).digest()[:4]
        return formated_privKey + checksum

    def generatePrivateKey(self):
        number = int(secrets.randbelow(1 << 256))
        while number == 0 or number > 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140:
            number = secrets.randbelow(1 << 256)
        return binascii.hexlify(number.to_bytes(32, byteorder='big'))
