import binascii
import hashlib
import base58
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from utils import *
from publicKey import *

class BitcoinAddress:
    def __init__(self, pubKey):
        self.p2pkh = self.generate_P2PKH(pubKey)
        self.p2pkh_compressed = self.generate_P2PKH_compressed(pubKey)
        self.p2psh_p2wpkh = self.generate_P2PSH(self.p2wpkh_witnessProgram(pubKey))
        self.p2psh_p2wpsh = self.generate_P2PSH(self.p2wpsh_witnessProgram(pubKey))
        self.p2psh_p2pkh = self.generate_P2PSH(self.p2pkh_redeemScript(pubKey))
        self.p2psh_p2multisig = self.generate_P2PSH(self.p2multisig_redeemScript(pubKey))

    def get(self, format="classic"):
        if format.upper() == "CLASSIC":
            return self.p2pkh
        elif format.upper() == "COMPRESSED":
            return self.p2pkh_compressed
        elif format.upper() == "P2SH-P2PKH":
            return (self.p2psh_p2pkh[0], self.p2psh_p2pkh[1])
        elif format.upper() == "P2SH-P2WPKH":
            return (self.p2psh_p2wpkh[0], self.p2psh_p2wpkh[1])
        elif format.upper() == "P2SH-P2WPSH":
            return (self.p2psh_p2wpsh[0], self.p2psh_p2wpsh[1])
        elif format.upper() == "P2SH-P2MULTISIG":
            return (self.p2psh_p2multisig[0], self.p2psh_p2multisig[1])
        else:
            raise BaseException("Error: Address format %s is not valid."%(format))

#################
# ADDRESSES     #
#################
    def generate_P2PKH(self, pubKey):
        address_version_byte = binascii.unhexlify("00")
        uncompress_pkey = binascii.unhexlify(pubKey.get(format="uncompressed"))
        addr_without_checksum = address_version_byte + hash160(uncompress_pkey).digest()
        btc_addr = base58.b58encode_check(addr_without_checksum)
        return btc_addr

    def generate_P2PKH_compressed(self, pubKey):
        address_version_byte = binascii.unhexlify("00")
        compress_pkey = binascii.unhexlify(pubKey.get(format="compressed"))
        addr_without_checksum = address_version_byte + hash160(compress_pkey).digest()
        btc_addr = base58.b58encode_check(addr_without_checksum)
        return btc_addr

    def generate_P2PSH(self, redeemScript):
        address_version_byte = binascii.unhexlify("05")
        addr_without_checksum = address_version_byte + hash160(redeemScript).digest()
        checksum = doubleSHA256(addr_without_checksum).digest()[:4]
        return (addr_without_checksum + checksum, redeemScript)

#####################
# REDEEM SCRIPTS    #
#####################
    def p2pkh_redeemScript(self, pubKey):
        #OP_DUP OP_HASH160 <PubkeyHash> OP_EQUALVERIFY OP_CHECKSIG
        compressed_pkey = binascii.unhexlify(pubKey.get(format="compressed"))
        redeemScript = binascii.unhexlify("76" + "a9" + "14") + hash160(compressed_pkey).digest() + binascii.unhexlify("88" + "ac")
        return redeemScript

    def p2multisig_redeemScript(self, pubKey):
        #<OP_2> <A pubkey> <B pubkey> <C pubkey> <OP_3> OP_CHECKMULTISIG
        uncompressed_pkey = binascii.unhexlify(pubKey.get(format="uncompressed"))
        redeemScript = binascii.unhexlify("51" + "41") + uncompressed_pkey + binascii.unhexlify("51" + "ae")
        return redeemScript

    def p2wpkh_witnessProgram(self, pubKey):
        compressed_pkey = binascii.unhexlify(pubKey.get(format="compressed"))
        (version_byte, pubkey_size_byte) = ("00", "14")
        v0_witnessProgram = binascii.unhexlify(version_byte + pubkey_size_byte) + hash160(compressed_pkey).digest()
        return v0_witnessProgram

    def p2wpsh_witnessProgram(self, pubKey):
        compressed_pkey = binascii.unhexlify(pubKey.get(format="compressed"))
        witness_script = binascii.unhexlify("76" + "a9") + hash160(compressed_pkey).digest() + binascii.unhexlify("88" + "ac")
        (version_byte, pubkey_size_byte) = ("00", "20")
        v0_witnessProgram = binascii.unhexlify(version_byte + pubkey_size_byte) + sha256(witness_script).digest()
        return v0_witnessProgram