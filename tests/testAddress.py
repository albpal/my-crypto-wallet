import unittest
from context import mycryptowallet
from mycryptowallet import address
import binascii
import base58
class TestAddress:
    def __init__(self, testunit):
        self.testunit = testunit
        return ;

    def test(self):
        _privKey=binascii.unhexlify("7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        addr = address.Address(privKey=_privKey)
        self.testunit.assertTrue(addr.getPrivKey().hex() == "7eb21e1fd7ce5a4b852443d88d0cb8042d44e2d0e435d536f6554babe7ece2ee")
        self.testunit.assertTrue(addr.getPubKey().hex() == "0497a470f28f8d76e2cf89835bcd57f26df366b69f9183789a05902ec3d72d73d354ac8300d012443551402cddabd660ca5432212357e628961596870f5ae7a659")
        self.testunit.assertTrue(addr.getAddress().decode() == "18mMPWwYhc8NY1B8LL2eGvPSQPZyxGWHQA")
