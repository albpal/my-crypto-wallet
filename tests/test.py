import unittest
from context import mycryptowallet
from mycryptowallet import address
from testAddress import TestAddress
from testWallet import TestWallet

class TestMyCryptoWallet(unittest.TestCase):
    def test_address(self):
        address = TestAddress(self)
        address.testAddressGeneration()
        address.testAddressSigning()

    def test_wallet(self):
        wallet = TestWallet(self)
        wallet.testCreateAddress()

if __name__ == '__main__':
    unittest.main()
