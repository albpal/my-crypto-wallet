import sys
import os
import binascii
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from address import Address
import plyvel
import base58

class Wallet:
    def __init__(self):
        self.db_path = os.path.dirname(__file__) + '/db'
    
    def createAddress(self):
        new_address = Address()
        db = plyvel.DB(self.db_path, create_if_missing=True)
        db.put(new_address.getAddress(), binascii.unhexlify(new_address.getPrivKey()), sync=True)
        db.close()
        self.showInfo(new_address)
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
    
    def importAddress(self, privKey):
        new_address = Address(privKey=privKey)
        db = plyvel.DB(self.db_path, create_if_missing=True)
        db.put(new_address.getAddress(), binascii.unhexlify(new_address.getPrivKey()), sync=True)
        db.close()
        self.showInfo(new_address)
        return new_address.getAddress().decode()

    def showInfo(self, addr):
        print(" > New address generated:")
        print("     Private key (raw hex):                      %s"%(addr.getPrivKey()))
        print("     Private key (WIF uncompressed format):      %s"%(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode()))
        print("     Private key (WIF compressed format):        %s"%(base58.b58encode(addr.getPrivKey(format="WIF-COMPRESSED")).decode()))
        print("     Public key (raw hex):                       %s"%(addr.getPubKey()))
        print("     Public key (compressed format):             %s"%(base58.b58encode(addr.getPubKey("compressed")).decode()))
        print("     Addresses by payment method:")
        print("         P2PK (uncompressed):                    %s"%(addr.getAddress().decode()))
        print("         P2PK (compressed):                      %s"%(addr.getAddress(format="compressed").decode()))
        print("         P2SH-P2PKH:")
        print("             Address:                            %s"%(base58.b58encode(addr.getAddress(format="P2SH-P2PKH")[0]).decode()))
        print("             RedeemSript:                        %s"%(addr.getAddress(format="P2SH-P2PKH")[1].hex()))
        print("         P2SH-P2MULTISIG:")
        print("             Address:                            %s"%(base58.b58encode(addr.getAddress(format="P2SH-P2MULTISIG")[0]).decode()))
        print("             RedeemSript:                        %s"%(addr.getAddress(format="P2SH-P2MULTISIG")[1].hex()))
        print("         P2SH-P2WPKH:")
        print("             Address:                            %s"%(base58.b58encode(addr.getAddress(format="P2SH-P2WPKH")[0]).decode()))
        print("             WitnessProgram:                     %s"%(addr.getAddress(format="P2SH-P2WPKH")[1].hex()))
        print("         P2SH-P2WPSH:")
        print("             Address:                            %s"%(base58.b58encode(addr.getAddress(format="P2SH-P2WPSH")[0]).decode()))
        print("             WitnessProgram:                     %s"%(addr.getAddress(format="P2SH-P2WPSH")[1].hex()))

def showHelpMain():
    print("\nwallet.py <action> <object>")
    print("     actions:")
    print("         create")
    print("         list")
    print("         delete")
    print("         import")
    print("   For more information use help in every action")
    print("\n")

def showHelpCreate():
    print("\nwallet.py create <object>")
    print("     objects:")
    print("         address -  creates and address")
    print("\n")

def showHelpImport():
    print("\nwallet.py create <object>")
    print("     objects:")
    print("         address -  Followed by private key to import. It can be binary (hex), WIF uncompress or WIF compress")
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

def parseActionImport():
    if len(sys.argv) < 4:
        showHelpImport()
        return
    if sys.argv[2] == "address":
        w = Wallet()
        w.importAddress(sys.argv[3])
    else:
        showHelpImport()

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
    elif sys.argv[1] == "import":
        parseActionImport()
    else:
        showHelpMain()

def execute():
    parseActions()

if len(sys.argv) == 1:
    showHelpMain()
else:
    execute()
