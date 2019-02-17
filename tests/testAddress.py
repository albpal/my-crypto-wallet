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
        self.testunit.assertEqual(addr.getAddress(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testAddressSigning(self):
        addr = address.Address()
        signature = addr.sign(bytes("data", 'utf-8'))
        self.testunit.assertTrue(addr.verify(bytes("data", 'utf-8'), signature))
        self.testunit.assertFalse(addr.verify(bytes("Data", 'utf-8'), signature))

    def testWIFUnCompressedFormat(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertEqual(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode(), "5Jn5rYMfc6JcgkLtr8XDosjoQzdr7X6sPXeFC5RuLbr6awAw9gK")
        self.testunit.assertEqual(addr.getAddress(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testWIFCompressedFormat(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertEqual(base58.b58encode(addr.getPrivKey(format="WIF-COMPRESSED")).decode(), "L1TzRfQDPtQkWSJoqrCPXtwuruPdmmruQSFPdtYv1WoheJ9FkGe2")
        self.testunit.assertEqual(addr.getAddress(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")

    def testCompressedPubkey(self):
        addr = address.Address(privKey="7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertEqual(addr.getPubKey("compressed"), "0397a470f28f8d76e2cf89835bcd57f26df366b69f9183789a05902ec3d72d73d3")
        self.testunit.assertEqual(addr.getAddress(), "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
    
    def testP2SH_P2WPKH(self):
        addr = address.Address(privKey="Kwc8fi8sqhC9zE8NWA61ajRrqvXW9Y4SPUhALCnytAPLFf3ao9fU")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "02b4f5f11110a51c4320646f8bd597ef22d5b6f24fb1f1c90d9fa4fd2c493d4672")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2WPKH")[0], "3H8275bQQ4x8nHM5vxFKXdZ7xWAEHq9HK5")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2WPKH")[1], "001409c48c894d9459608da59c0eb77c0a5fb970a949")

    def testP2SH_P2PKH(self):
        addr = address.Address(privKey="5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "0244182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa34")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2PKH")[0], "3Gttx49gcG8TKcApWVgH8bovDmEGp2zvZ3")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2PKH")[1], "76a91441b04df087fcec32ea1900f38fda3c14520428ef88ac")

    def testP2SH_P2MULTISIG(self):
        addr = address.Address(privKey="5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "0244182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa34")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2MULTISIG")[0], "3DiL5fRuXGSm6V6QgE227HRcxSqSJvGYrd")
        self.testunit.assertEqual(addr.getAddress(format="P2SH-P2MULTISIG")[1], "51410444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db051ae")

    def testP2WPKH(self):
        addr = address.Address(privKey="KwEhgwz9vbUyd8jPrJR5ix3tR17JPZbtgYDsJyva6cjdJe2dUhPf")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "03a6ea653ac66e71e58db0e80fbec3e24d6c1c864ea8865b52d79e40cceb4ae0e0")
        self.testunit.assertEqual(addr.getAddress(format="P2WPKH"), "bc1qapy3lv24qxz8fjps6z85asr7zv84j32ptq3jgf")

    def testP2WPSH_P2PKH(self):
        addr = address.Address(privKey="KwEhgwz9vbUyd8jPrJR5ix3tR17JPZbtgYDsJyva6cjdJe2dUhPf")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "03a6ea653ac66e71e58db0e80fbec3e24d6c1c864ea8865b52d79e40cceb4ae0e0")
        self.testunit.assertEqual(addr.getAddress(format="P2WSH-P2PKH")[0], "bc1q6n8p6ds3rtyla6cwrxkljqaj24gq64cv82smmaapd94pxh2szyvqhr7g4k")
        self.testunit.assertEqual(addr.getAddress(format="P2WSH-P2PKH")[1], "d4ce1d36111ac9feeb0e19adf903b255500d570c3aa1bdf7a1696a135d501118")
    
    def testP2WPSH_P2MULTISIG(self):
        addr = address.Address(privKey="KwEhgwz9vbUyd8jPrJR5ix3tR17JPZbtgYDsJyva6cjdJe2dUhPf")
        self.testunit.assertEqual(addr.getPubKey(format="compressed"), "03a6ea653ac66e71e58db0e80fbec3e24d6c1c864ea8865b52d79e40cceb4ae0e0")
        self.testunit.assertEqual(addr.getAddress(format="P2WSH-P2MULTISIG")[0], "bc1qqlcvm3xum9qfh0ettnanj98dnyye7a2emksm6enjzaw9f8sr3wusq4w3nx")
        self.testunit.assertEqual(addr.getAddress(format="P2WSH-P2MULTISIG")[1], "07f0cdc4dcd9409bbf2b5cfb3914ed99099f7559dda1bd6672175c549e038bb9")