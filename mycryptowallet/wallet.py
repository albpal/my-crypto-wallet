import sys
import os
import binascii
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from address import Address
import plyvel
import base58
import utils

class Wallet:
    def __init__(self):
        self.db_path = os.path.dirname(__file__) + '/db'
    
    def createAddress(self):
        new_address = Address()
        db = plyvel.DB(self.db_path, create_if_missing=True)
        db.put(new_address.getAddress().encode(), binascii.unhexlify(new_address.getPrivKey()), sync=True)
        db.close()
        self.showInfo(new_address)
        return new_address.getAddress()

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
        db.put(new_address.getAddress().encode(), binascii.unhexlify(new_address.getPrivKey()), sync=True)
        db.close()
        self.showInfo(new_address)
        return new_address.getAddress()

    def createMultisigAddressFromNone(self, n, m):
        pubKeys=[]
        for i in range(0, m):
            pubKey = input("Insert public key %i: "%(i+1))
            pubKeys.append(pubKey)
        msigAddr = Address()
        msigAddr.multisig(pubKeys, n=n, m=m)
        print("Bitcoin multisig address: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[0]))
        print("Bitcoin multisig redeem script: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[1]))

    def createMultisigAddressFromRNG(self, n, m):
        pubKeys=[]
        pubAddrs=[]
        for i in range(0, m):
            random=self.readRandomFromComputer()
            pubAddr = Address(privKey=random)
            pubAddrs.append(pubAddr)
            pubKeys.append(pubAddr.getPubKey(format="uncompressed"))
        msigAddr = Address()
        msigAddr.multisig(pubKeys, n=n, m=m)
        i=0
        for addr in pubAddrs:
            i=i+1
            print("\nAddress %i:"%(i))
            print("     Private key: %s"%(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode()))
            print("     Public key: %s\n"%(addr.getPubKey(format="uncompressed")))
        print("Bitcoin multisig address: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[0]))
        print("Bitcoin multisig redeem script: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[1]))

    def readRandomFromComputer(self):
        addr = Address()
        return addr.getPrivKey()

    def readRandomFromInput(self, i):
        random = input("Insert random numbers for private key %i: "%(i+1))
        random = random.replace(" ", "").encode('utf-8')
        return binascii.hexlify(utils.sha256(random).digest())

    def createAddressFromBoth(self, n, m):
        pubKeys=[]
        pubAddrs=[]
        for i in range(0, m):
            str1=self.readRandomFromComputer().decode("utf-8")
            str2=self.readRandomFromInput(i).decode("utf-8")
            if len(str1) != len(str2):
                raise Exception("The two generated random numbers have not the same length")
            random1 = int(str1, 16)
            random2 = int(str2, 16)
            random = hex(random1 ^ random2)[2:].zfill(64)
            pubAddr = Address(privKey=random)
            pubAddrs.append(pubAddr)
            pubKeys.append(pubAddr.getPubKey(format="uncompressed"))
        msigAddr = Address()
        msigAddr.multisig(pubKeys, n=n, m=m)
        i=0
        for addr in pubAddrs:
            i=i+1
            print("\nAddress %i:"%(i))
            print("     Private key: %s"%(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode()))
            print("     Public key: %s\n"%(addr.getPubKey(format="uncompressed")))
        print("Bitcoin multisig address: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[0]))
        print("Bitcoin multisig redeem script: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[1]))
        
    def createMultisigAddressFromInput(self, n, m):
        pubKeys=[]
        pubAddrs=[]
        for i in range(0, m):
            random=self.readRandomFromInput(i)
            pubAddr = Address(privKey=random)
            pubAddrs.append(pubAddr)
            pubKeys.append(pubAddr.getPubKey(format="uncompressed"))
        msigAddr = Address()
        msigAddr.multisig(pubKeys, n=n, m=m)
        i=0
        for addr in pubAddrs:
            i=i+1
            print("\nAddress %i:"%(i))
            print("     Private key: %s"%(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode()))
            print("     Public key: %s\n"%(addr.getPubKey(format="uncompressed")))
        print("Bitcoin multisig address: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[0]))
        print("Bitcoin multisig redeem script: %s"%(msigAddr.getAddress(format="P2SH-P2MULTISIG")[1]))
        
    def createMultisigAddress(self, n, m, entropy_source):
        if entropy_source == "none":
            self.createMultisigAddressFromNone(n, m)
        elif entropy_source == "rng":
            self.createMultisigAddressFromRNG(n, m)
        elif entropy_source == "input":
            self.createMultisigAddressFromInput(n, m)
        elif entropy_source == "both":
            self.createAddressFromBoth(n, m)

    def showInfo(self, addr):
        print(" > New address generated:")
        print("     Private key (raw hex):                      %s"%(addr.getPrivKey()))
        print("     Private key (WIF uncompressed format):      %s"%(base58.b58encode(addr.getPrivKey(format="WIF-UNCOMPRESSED")).decode()))
        print("     Private key (WIF compressed format):        %s"%(base58.b58encode(addr.getPrivKey(format="WIF-COMPRESSED")).decode()))
        print("     Public key (raw hex):                       %s"%(addr.getPubKey()))
        print("     Public key (compressed format):             %s"%(base58.b58encode(addr.getPubKey("compressed")).decode()))
        print("     Addresses by payment method:")
        print("         P2PKH (uncompressed):                   %s"%(addr.getAddress()))
        print("         P2PKH (compressed):                     %s"%(addr.getAddress(format="compressed")))
        print("         P2SH:")
        print("             P2PKH:")
        print("                 Address:                        %s"%(addr.getAddress(format="P2SH-P2PKH")[0]))
        print("                 RedeemSript:                    %s"%(addr.getAddress(format="P2SH-P2PKH")[1]))
        print("             P2MULTISIG (one-of-one):")
        print("                 Address:                        %s"%(addr.getAddress(format="P2SH-P2MULTISIG")[0]))
        print("                 RedeemSript:                    %s"%(addr.getAddress(format="P2SH-P2MULTISIG")[1]))
        print("             P2WPKH:")
        print("                 Address:                        %s"%(addr.getAddress(format="P2SH-P2WPKH")[0]))
        print("                 WitnessProgram:                 %s"%(addr.getAddress(format="P2SH-P2WPKH")[1]))
        print("         P2WPKH:                                 %s"%(addr.getAddress(format="P2WPKH")))
        print("         P2WSH:")
        print("             P2PKH:")
        print("                 Address:                        %s"%(addr.getAddress(format="P2WSH-P2PKH")[0]))
        print("                 WitnessProgram:                 %s"%(addr.getAddress(format="P2WSH-P2PKH")[1]))
        print("             P2MULTISIG (one-of-one):")
        print("                 Address:                        %s"%(addr.getAddress(format="P2WSH-P2MULTISIG")[0]))
        print("                 WitnessProgram:                 %s"%(addr.getAddress(format="P2WSH-P2MULTISIG")[1]))

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
    print("         multisig n m <entropy_source> (rng, input, rng_input, none)-  creates and address")
    print("                 entropy_source:")
    print("                     rng: Generates all addresses by you using system randomness")
    print("                     input: Asks you random numbers which derive private keys, etc.")
    print("                     rng_input: XOR of an rng generation and the input given by the user")
    print("                     none: Asks you for the public keys")
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
    elif sys.argv[2] == "multisig":
        if len(sys.argv) < 6:
            showHelpCreate()
            return
        n = int(sys.argv[3])
        m = int(sys.argv[4])
        entropy_source= sys.argv[5]
        w = Wallet()
        w.createMultisigAddress(n, m, entropy_source)

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
