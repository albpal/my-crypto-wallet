import unittest
from context import mycryptowallet
from mycryptowallet import wallet
import binascii
import base58
class TestWallet:
    def __init__(self, testunit):
        self.testunit = testunit
        return ;

    def testCreateAddress(self):
        w = wallet.Wallet()
        btc_address=w.createAddress()
        self.testunit.assertTrue(btc_address[0] == "1")
        w.deleteAddress("all")

    def testListAddress(self):
        w = wallet.Wallet()
        btc_address1=w.createAddress()
        btc_address2=w.createAddress()
        addresses=w.listAddresses()
        self.testunit.assertTrue(btc_address1 in addresses)
        self.testunit.assertTrue(btc_address2 in addresses)
        w.deleteAddress(btc_address1)
        addresses=w.listAddresses()
        self.testunit.assertFalse(btc_address1 in addresses)
        w.deleteAddress("all")
    
    def testImportAddress(self):
        w = wallet.Wallet()
        btc_address1=w.importAddress("5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny")
        addresses=w.listAddresses()
        self.testunit.assertTrue("19LH6eahzaBVU9rz6TK81rUJ8ZfdyAsM3S" in addresses)
        w.deleteAddress("all")



