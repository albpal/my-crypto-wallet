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
        self.testunit.assertEqual(addr.getPrivKey(), "7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertEqual(addr.getPubKey(), "0497a470f28f8d76e2cf89835bcd57f26df366b69f9183789a05902ec3d72d73d354ac8300d012443551402cddabd660ca5432212357e628961596870f5ae7a659")
        self.testunit.assertEqual(addr.getAddress().decode(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testAddressSigning(self):
        addr = address.Address()
        signature = addr.sign(bytes("data", 'utf-8'))
        self.testunit.assertTrue(addr.verify(bytes("data", 'utf-8'), signature))
        self.testunit.assertFalse(addr.verify(bytes("Data", 'utf-8'), signature))

    def testWIFUnCompressedFormat(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertEqual(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode(), "5Jn5rYMfc6JcgkLtr8XDosjoQzdr7X6sPXeFC5RuLbr6awAw9gK")
        self.testunit.assertEqual(addr.getAddress().decode(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testWIFCompressedFormat(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertEqual(base58.b58encode(addr.getPrivKey(format="WIF-COMPRESSED")).decode(), "L1TzRfQDPtQkWSJoqrCPXtwuruPdmmruQSFPdtYv1WoheJ9FkGe2")
        self.testunit.assertEqual(addr.getAddress().decode(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")

    def testCompressedPubkey(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertEqual(addr.getPubKey("compressed"), "0397a470f28f8d76e2cf89835bcd57f26df366b69f9183789a05902ec3d72d73d3")
        self.testunit.assertEqual(addr.getAddress().decode(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testP2SH_P2WPKH(self):
        addr = address.Address(privKey="Kwc8fi8sqhC9zE8NWA61ajRrqvXW9Y4SPUhALCnytAPLFf3ao9fU")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "02b4f5f11110a51c4320646f8bd597ef22d5b6f24fb1f1c90d9fa4fd2c493d4672")
        self.testunit.assertEqual(base58.b58encode(addr.getAddress(format="P2SH-P2WPKH")[0]).decode(), "3H8275bQQ4x8nHM5vxFKXdZ7xWAEHq9HK5")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2WPKH")[1].hex(), "001409c48c894d9459608da59c0eb77c0a5fb970a949")

    def testP2SH_P2WPSH(self):
        addr = address.Address(privKey="Kwc8fi8sqhC9zE8NWA61ajRrqvXW9Y4SPUhALCnytAPLFf3ao9fU")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "02b4f5f11110a51c4320646f8bd597ef22d5b6f24fb1f1c90d9fa4fd2c493d4672")
        self.testunit.assertEqual(base58.b58encode(addr.getAddress(format="P2SH-P2WPSH")[0]).decode(), "3HcdsKUhbgGcwuUXnjpxLp4QtMDysf2kpA")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2WPSH")[1].hex(), "00208ea727708ea3c3cf8b7b881e9f7fc6703792b348c224980473dadc019d656d2f")

    def testP2SH_P2PKH(self):
        addr = address.Address(privKey="5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "0244182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa34")
        self.testunit.assertEqual(base58.b58encode(addr.getAddress(format="P2SH-P2PKH")[0]).decode(), "3Gttx49gcG8TKcApWVgH8bovDmEGp2zvZ3")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2PKH")[1].hex(), "76a91441b04df087fcec32ea1900f38fda3c14520428ef88ac")

    def testP2SH_P2MULTISIG(self):
        addr = address.Address(privKey="5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "0244182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa34")
        self.testunit.assertEqual(base58.b58encode(addr.getAddress(format="P2SH-P2MULTISIG")[0]).decode(), "3DiL5fRuXGSm6V6QgE227HRcxSqSJvGYrd")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2MULTISIG")[1].hex(), "51410444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db051ae")