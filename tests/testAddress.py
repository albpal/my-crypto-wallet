import unittest
from context import mycryptowallet
from mycryptowallet import address
import binascii
import base58
class TestAddress:
    def __init__(self, testunit):
        self.testunit = testunit
        return ;

    def testAddressGeneration(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertTrue(addr.getPrivKey().hex() == "7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertTrue(addr.getPubKey().hex() == "0497a470f28f8d76e2cf89835bcd57f26df366b69f9183789a05902ec3d72d73d354ac8300d012443551402cddabd660ca5432212357e628961596870f5ae7a659")
        self.testunit.assertTrue(addr.getAddress().decode() == "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testAddressSigning(self):
        addr = address.Address()
        signature = addr.sign(bytes("data", 'utf-8'))
        self.testunit.assertTrue(addr.verify(bytes("data", 'utf-8'), signature))
        self.testunit.assertFalse(addr.verify(bytes("Data", 'utf-8'), signature))

    def testWIFUnCompressedFormat(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertTrue(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode() == "5Jn5rYMfc6JcgkLtr8XDosjoQzdr7X6sPXeFC5RuLbr6awAw9gK")
        self.testunit.assertTrue(addr.getAddress().decode() == "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testWIFCompressedFormat(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertTrue(base58.b58encode(addr.getPrivKey(format="WIF-COMPRESSED")).decode() == "L1TzRfQDPtQkWSJoqrCPXtwuruPdmmruQSFPdtYv1WoheJ9FkGe2")
        self.testunit.assertTrue(addr.getAddress().decode() == "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")

    def testCompressedPubkey(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertTrue(base58.b58encode(addr.getPubKey("compressed")).decode() == "24tu7CXWBB7guwNo3FvSA4T1YfxY6EhrufqfamQ8z8KRL")
        self.testunit.assertTrue(addr.getAddress().decode() == "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testP2SH(self):
        addr = address.Address(privKey="Kwc8fi8sqhC9zE8NWA61ajRrqvXW9Y4SPUhALCnytAPLFf3ao9fU")
        self.testunit.assertTrue(addr.getPubKey(format="compressed").hex() == "02b4f5f11110a51c4320646f8bd597ef22d5b6f24fb1f1c90d9fa4fd2c493d4672")
        self.testunit.assertTrue(base58.b58encode(addr.getAddress(format="p2sh")).decode() == "3H8275bQQ4x8nHM5vxFKXdZ7xWAEHq9HK5")
        self.testunit.assertTrue(addr.getAddress(format="redeem").hex() == "001409c48c894d9459608da59c0eb77c0a5fb970a949")

