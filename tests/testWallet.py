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
        self.testunit.assertTrue(btc_address.decode()[0] == "1")




