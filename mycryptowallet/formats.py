import binascii
import hashlib
import base58
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from utils import *

class Format:
    def __init__(self, format):
        if format.upper() == "SEGWIT":
            raise("Function to be done.")
        elif format.upper() == "CLASSIC":
            self.format_func = AddressFormat.classic
        elif format.upper() == "P2SH":
            self.format_func = AddressFormat.p2shFormat
        elif format.upper() == "REDEEM":
            self.format_func = AddressFormat.redeemScript
        elif format.upper() == "COMPRESSED":
            self.format_func = PublicKeyFormat.compressedFormat
        elif format.upper() == "UNCOMPRESSED":
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
    def classic(pubKey):
        uncompress_pkey = Format(format="uncompressed").format(pubKey)
        pubKeySHA256 = hashlib.sha256(uncompress_pkey).digest()
        hash160 = ripemd160(pubKeySHA256).digest()
        addr_without_checksum = binascii.unhexlify("00") + hash160
        # checksum = hashlib.sha256(hashlib.sha256(addr_without_checksum).digest()).digest()[:4]
        btc_addr = base58.b58encode_check(addr_without_checksum)
        return btc_addr

    def redeemScript(pubKey):
        compressed_pkey = Format(format="compressed").format(pubKey)
        pubKeySHA256 = hashlib.sha256(compressed_pkey).digest()
        redeem_script = binascii.unhexlify("0014") + ripemd160(pubKeySHA256).digest()
        return redeem_script

    def p2shFormat(pubKey):
        redeem_script = AddressFormat.redeemScript(pubKey)
        addr_without_checksum = binascii.unhexlify("05") + hash160(redeem_script).digest()
        checksum = hashlib.sha256(hashlib.sha256(addr_without_checksum).digest()).digest()[:4]
        return addr_without_checksum + checksum

class PublicKeyFormat:
    def uncompressedFormat(pubKey):
        return binascii.unhexlify("04") + pubKey

    def compressedFormat(pubKey):
        x = binascii.hexlify(pubKey)[:64]
        y = binascii.hexlify(pubKey)[64:]
        if int(y,base=16) % 2 == 0:
            prefix = binascii.unhexlify("02")
        else:
            prefix = binascii.unhexlify("03")
        return prefix + binascii.unhexlify(x)

class PrivateKeyFormat:
    def standardFormat(privKey):
        return privKey
    
    def WIFUncompressedFormat(privKey):
        mainnet_address = binascii.unhexlify("80") + privKey
        checksum = hashlib.sha256(hashlib.sha256(mainnet_address).digest()).digest()[:4]
        return mainnet_address + checksum

    def WIFCompressedFormat(privKey):
        mainnet_address = binascii.unhexlify("80") + privKey + binascii.unhexlify("01")
        checksum = hashlib.sha256(hashlib.sha256(mainnet_address).digest()).digest()[:4]
        return mainnet_address + checksum
