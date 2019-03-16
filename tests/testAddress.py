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
        addr1 = address.Address(privKey="5JAwK9bihMRFe9zw32csUUEn7N5MvLvuwXKv5qUnQVjbthZyuwQ")
        addr2 = address.Address(privKey="5KC6MNFkqN665YAbb1wrveGWmygainm99wX8fSxA779UZh3yP2t")
        addr3 = address.Address(privKey="5J4DNddHjUkSoG2GZAkxwqmz1T5TTVbnf7Q5ho8Eqkinbc2hvSe")
        addr4 = address.Address(privKey="5K7idDARSfWLGjA926DFvVL8igZANsJsUcGo8vztmPH45iScp8K")

        pubKey1 = addr1.getPubKey(format="uncompressed")
        pubKey2 = addr2.getPubKey(format="uncompressed")
        pubKey3 = addr3.getPubKey(format="uncompressed")
        pubKey4 = addr4.getPubKey(format="uncompressed")

        msigAddr = address.Address()
        msigAddr.multisig([pubKey1, pubKey2, pubKey3, pubKey4], n=2, m=4)

        self.testunit.assertEqual(msigAddr.getAddress(format="P2SH-P2MULTISIG")[0], "3Hy6A3rSXKRumyVqURBoiv4QpQLt6vMCzt")
        self.testunit.assertEqual(msigAddr.getAddress(format="P2SH-P2MULTISIG")[1], "524104fe0fcd054a31130749467f07e272426f7dd7a3029ab5b076d7285a931bd131d34ed9f28b2cc2fe266aa62c4cada3e82b70a4416966902201c4d73759f7f0425e41044f2ec9f80ef2c4f385f3d27b6167f77236de63548723ba1c90a324f4ec46dfd14a2fba5a9c048a5ec310aedfe875d8a254f336e8f7d5d17338d9451dc6f2188c4104aefb86098442adc6c3dffd9b0e27fe8e918462469a5ec5363e26920f09facea70b63e4f4d2736089286d4dd2352ca65016e7d593f105009f9a35c03a2464aa20410451e7f31ea2f5cb14ba76ca20952c1d453fe3a85959ebbefee8912ad6f74c443a03e52ef8a842f890f1ab2d69c6bb418e6de0f15bef944be2883887be3bb75cc054ae")

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