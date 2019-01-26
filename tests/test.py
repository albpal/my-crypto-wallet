import unittest
from context import mycryptowallet
from mycryptowallet import address
from testAddress import TestAddress

class TestMyCryptoWallet(unittest.TestCase):
    def test_address(self):
        address = TestAddress(self)
        address.test()

if __name__ == '__main__':
    unittest.main()
