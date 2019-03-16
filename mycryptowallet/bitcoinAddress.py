import binascii
import hashlib
import base58
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from utils import *
from publicKey import *

class BitcoinAddress:
    def __init__(self, pubKey=[], n=1, m=1):
        if isinstance(pubKey, list):
            if len(pubKey) < 2:
                raise Exception("Multisig addresses must have at least 2 public keys")
            self.p2sh_p2multisig = self.get_address_for_P2PSH_payments(self.p2multisig_script(pubKey, n=n, m=m))
            self.p2wsh_p2multisig = self.get_address_for_nativeSegwit_P2WPSH_payments(self.p2multisig_script(pubKey, n=n, m=m))
        else:
            self.p2pkh = self.get_address_for_P2PKH_payments(pubKey, compressed=False)
            self.p2pkh_compressed = self.get_address_for_P2PKH_payments(pubKey, compressed=True)
            self.p2sh_p2wpkh = self.get_address_for_P2PSH_payments(self.p2wpkh_witnessProgram_for_p2sh(pubKey))
            self.p2sh_p2pkh = self.get_address_for_P2PSH_payments(self.p2pkh_script(pubKey))
            self.p2sh_p2multisig = self.get_address_for_P2PSH_payments(self.p2multisig_script([pubKey.get()]))
            self.p2wpkh = self.get_address_for_P2PKH_payments(pubKey, compressed=True, encoding="bech32")
            self.p2wsh_p2pkh = self.get_address_for_nativeSegwit_P2WPSH_payments(self.p2pkh_script(pubKey))
            self.p2wsh_p2multisig = self.get_address_for_nativeSegwit_P2WPSH_payments(self.p2multisig_script([pubKey.get()]))

    def get(self, format="P2PKH"):
        if format.upper() == "P2PKH":
            return self.p2pkh
        elif format.upper() == "COMPRESSED":
            return self.p2pkh_compressed
        elif format.upper() == "P2SH-P2PKH":
            return (self.p2sh_p2pkh[0], self.p2sh_p2pkh[1])
        elif format.upper() == "P2SH-P2WPKH":
            return (self.p2sh_p2wpkh[0], self.p2sh_p2wpkh[1])
        elif format.upper() == "P2SH-P2MULTISIG":
            return (self.p2sh_p2multisig[0], self.p2sh_p2multisig[1])
        elif format.upper() == "P2WPKH":
            return self.p2wpkh
        elif format.upper() == "P2WSH-P2PKH":
            return (self.p2wsh_p2pkh[0], self.p2wsh_p2pkh[1])
        elif format.upper() == "P2WSH-P2MULTISIG":
            return (self.p2wsh_p2multisig[0], self.p2wsh_p2multisig[1])
        else:
            raise BaseException("Error: Address format %s is not valid."%(format))

#################
#   ADDRESSES   #
#################
    def get_address_for_P2PKH_payments(self, pubKey, compressed=True, encoding="base58", addr_version=0):
        if compressed:
            pubkey_hex = binascii.unhexlify(pubKey.get(format="compressed"))
        else:
            pubkey_hex = binascii.unhexlify(pubKey.get(format="uncompressed"))

        hashed_key = hash160(pubkey_hex).digest()

        if encoding == "base58":#BIP16 base58 encoding
            btc_addr = base58.b58encode_check(addr_version.to_bytes(1, byteorder="big") + hashed_key).decode()
        elif encoding == "bech32":#BIP141 segwit base32 checksum aka bech32 encoding
            if not compressed:
                raise BaseException("Bech32 encoding only supports compressed public keys")
            btc_addr = segwit_encode("bc", addr_version, hashed_key)

        return btc_addr

    def get_address_for_P2PSH_payments(self, redeemScript, encoding="base58"):
        address_version_byte = binascii.unhexlify("05")
        addr_without_checksum = address_version_byte + hash160(binascii.unhexlify(redeemScript)).digest()
        checksum = doubleSHA256(addr_without_checksum).digest()[:4]
        btc_addr = base58.b58encode_check(addr_without_checksum)
        return (btc_addr.decode(), redeemScript)

    def get_address_for_nativeSegwit_P2WPSH_payments(self, witnessProgram):
        # https://bitcointalk.org/index.php?topic=4992632.0
        # https://github.com/sipa/bech32/blob/master/ref/python/segwit_addr.py
        hrp = "bc"
        wit_version_byte = 0

        v0_witnessProgram = sha256(binascii.unhexlify(witnessProgram)).digest()
        witnessProgram = binascii.hexlify(v0_witnessProgram).decode()

        address = segwit_encode(hrp, wit_version_byte, v0_witnessProgram)
        return (address, binascii.hexlify(v0_witnessProgram).decode())

########################################
#       STANDARD SCRIPTS               #
########################################
    def p2pkh_script(self, pubKey):
        compressed_pubkey = binascii.unhexlify(pubKey.get(format="compressed"))
        (O_DUP, OP_HASH160, PubkeyHash, OP_EQUALVERIFY, OP_CHECKSIG) = (binascii.unhexlify("76"), binascii.unhexlify("a9"), binascii.unhexlify("14") + hash160(compressed_pubkey).digest(), binascii.unhexlify("88"), binascii.unhexlify("ac"))
        redeemScript = O_DUP + OP_HASH160 + PubkeyHash + OP_EQUALVERIFY + OP_CHECKSIG
        return binascii.hexlify(redeemScript).decode()

    def p2multisig_script(self, pubKeyList, n=1, m=1):
        #<OP_2> <A pubkey> <B pubkey> <C pubkey> <OP_3> OP_CHECKMULTISIG
        redeemScript = binascii.unhexlify(hex(n + 80)[2:])

        uncompressed_pubkey = binascii.unhexlify("41") + binascii.unhexlify(pubKeyList[0].encode('utf-8'))
        redeemScript = redeemScript + uncompressed_pubkey

        for pubKey in pubKeyList[1:]:
            uncompressed_pubkey = binascii.unhexlify("41") + binascii.unhexlify(pubKey.encode('utf-8'))
            redeemScript = redeemScript + uncompressed_pubkey

        redeemScript = redeemScript + binascii.unhexlify(hex(m + 80)[2:]) + binascii.unhexlify("ae")
        return binascii.hexlify(redeemScript).decode()

    def p2wpkh_witnessProgram_for_p2sh(self, pubKey):
        compressed_pkey = binascii.unhexlify(pubKey.get(format="compressed"))
        (version_byte, pubkey_size_byte) = ("00", "14")
        v0_witnessProgram = binascii.unhexlify(version_byte + pubkey_size_byte) + hash160(compressed_pkey).digest()
        return binascii.hexlify(v0_witnessProgram).decode()
