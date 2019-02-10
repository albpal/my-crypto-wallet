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
        address.testWIFCompressedFormat()
        address.testWIFUnCompressedFormat()
        address.testCompressedPubkey()
        address.testP2SH_P2WPKH()
        address.testP2SH_P2WPSH()
        address.testP2SH_P2PKH()

    def test_wallet(self):
        wallet = TestWallet(self)
        wallet.testCreateAddress()
        wallet.testListAddress()
        wallet.testImportAddress()
    

if __name__ == '__main__':
    unittest.main()
