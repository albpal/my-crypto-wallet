import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from address import Address
import plyvel

class Wallet:
    def __init__(self):
        self.db_path = os.path.dirname(__file__) + '/db'
    
    def createAddress(self):
        new_address = Address()
        db = plyvel.DB(self.db_path, create_if_missing=True)
        db.put(new_address.getAddress(), new_address.getPrivKey(), sync=True)
        db.close()
        print(" > New address generated (raws are binary, the others are in base58 encoded):")
        print("     Private key (raw):                        %s"%(new_address.getPrivKey().hex()))
        print("     Private key (WIF uncompressed format):    %s"%(new_address.getPrivKey(format="WIF-UNCOMPRESSED").decode()))
        print("     Private key (WIF compressed format):      %s"%(new_address.getPrivKey(format="WIF-COMPRESSED").decode()))
        print("     Public key (raw):                         %s"%(new_address.getPubKey().hex()))
        print("     Public key (compressed format):           %s"%(new_address.getPubKey("compressed").decode()))
        print("     Bitcoin address:                          %s"%(new_address.getAddress().decode()))
        return new_address.getAddress().decode()

    def listAddresses(self):
        addresses = []
        db = plyvel.DB(self.db_path, create_if_missing=True)
        i = 0
        for key, value in db:
            print("Address %i: %s"%(i, key))
            addresses.append(key.decode())
            i=i+1
        db.close()
        return addresses

    def deleteAddress(self, address):
        db = plyvel.DB(self.db_path, create_if_missing=True)
        if address == "all":
            for key, value in db:
                db.delete(key, sync=True)
        else:
            db.delete(address.encode(), sync=True)
        db.close()

def showHelpMain():
    print("\nwallet.py <action> <object>")
    print("     actions:")
    print("         create")
    print("         list")
    print("         delete")
    print("   For more information use help in every action")
    print("\n")

def showHelpCreate():
    print("\nwallet.py create <object>")
    print("     objects:")
    print("         address -  creates and address")
    print("\n")

def showHelpDelete():
    print("\nwallet.py delete <object>")
    print("     objects:")
    print("         address - deletes one or more addresses. all delete all addresses")
    print("\n")

def showHelpList():
    print("\nwallet.py list <object>")
    print("     objects:")
    print("         addresses - List addresses stored in wallet")
    print("\n")

def parseActionCreate():
    if len(sys.argv) < 3:
        showHelpCreate()
        return
    if sys.argv[2] == "address":
        w = Wallet()
        w.createAddress()
    else:
        showHelpCreate()

def parseActionList():
    if len(sys.argv) < 3:
        showHelpList()
        return
    if sys.argv[2] == "addresses":
        w = Wallet()
        w.listAddresses()
    else:
        showHelpList()

def parseActionDelete():
    if len(sys.argv) < 3:
        showHelpDelete()
        return
    if sys.argv[2] == "address":
        w = Wallet()
        for address in sys.argv[3:]:
            w.deleteAddress(address)
    else:
            showHelpDelete()

def parseActions():
    if sys.argv[1] == "create":
        parseActionCreate()
    elif sys.argv[1] == "delete":
        parseActionDelete()
    elif sys.argv[1] == "list":
        parseActionList()
    else:
        showHelpMain()

def execute():
    parseActions()

if len(sys.argv) == 1:
    showHelpMain()
else:
    execute()
