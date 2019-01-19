import unittest
from context import mycryptowallet
from mycryptowallet import address

class TestMyCryptoWallet(unittest.TestCase):
	def test_dummyTest(self):
		wallete = address.Address()
		wallete.foo()
		self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
