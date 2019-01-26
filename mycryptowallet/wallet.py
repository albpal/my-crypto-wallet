import sys
from address import Address

class Wallet:
    def __init(self):
        addresses = {}
    
    def createAddress(self):
        new_address = Address()
        print("#### New address generated ####")
        print("     Private key (standard format):  %s"%(new_address.getPrivKey().hex()))
        print("     Public key (uncompress format): %s"%(new_address.getPubKey().hex()))
        print("     Bitcoin address:                %s"%(new_address.getAddress().decode()))
        return new_address.getAddress()

def showHelp():
    print("\nwallet.py <action> <object>")
    print("     actions:")
    print("         create - Creates an object")
    print("     objects")
    print("         address - Creates a bitcoin address")
    print("\n")

def execute():
    if sys.argv[1] == "create":
        if sys.argv[2] == "address":
            w = Wallet()
            w.createAddress()
        else:
            showHelp()
    else:
        showHelp()

if len(sys.argv) == 0:
    showHelp()
else:
    execute()
