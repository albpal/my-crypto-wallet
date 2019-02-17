[![Build Status](http://37.247.52.181:8080/buildStatus/icon?job=mycryptowallet)](http://37.247.52.181:8080/job/mycryptowallet/)
# my-crypto-wallet
Simple wallet I'm building for learning purposes. To use it (Python 3.6 or higher):

```
python mycryptowallet/wallet.py create address

> New address generated:
     Private key (raw hex):                      b'3e1258347b897fee4055b0ae9f59b459f31905815e9214bfddede6990f73b36f'
     Private key (WIF uncompressed format):      5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny
     Private key (WIF compressed format):        KyJNRBYQRJJDz2FPkc6ei5FaUerSt1JegV3o4vFxEt4P924VYdTn
     Public key (raw hex):                       0444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db0
     Public key (compressed format):             Kmo8qPN3sHiGata4QN9zx5Rda6H8ML2yRqXj42DtAgarfVYHMtprMSynLYQ6pQYjn4347xraQQe3GSEBQY2AugffKh
     Addresses by payment method:
         P2PKH (uncompressed):                   19LH6eahzaBVU9rz6TK81rUJ8ZfdyAsM3S
         P2PKH (compressed):                     16zL8KPTGraBuhHeQymiZmWcRrD92vBBNj
         P2SH:
             P2PKH:
                 Address:                        3Gttx49gcG8TKcApWVgH8bovDmEGp2zvZ3
                 RedeemSript:                    76a91441b04df087fcec32ea1900f38fda3c14520428ef88ac
             P2MULTISIG (one-of-one):
                 Address:                        3DiL5fRuXGSm6V6QgE227HRcxSqSJvGYrd
                 RedeemSript:                    51410444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db051ae
             P2WPKH:
                 Address:                        3K3utwxrfhcNvaVznLR261sWBdt3z4BMoF
                 WitnessProgram:                 001441b04df087fcec32ea1900f38fda3c14520428ef
         P2WPKH:                                 bc1qgxcymuy8lnkr96seqreclk3uz3fqg280rxgrr8
         P2WSH:
             P2PKH:
                 Address:                        bc1qjdfsfyjf6kf7pm3ud57scnr34jadlcfkn4720tmlydl9cetakfyqne26ah
                 WitnessProgram:                 9353049249d593e0ee3c6d3d0c4c71acbadfe1369d7ca7af7f237e5c657db248
             P2MULTISIG (one-of-one):
                 Address:                        bc1q2nu8ey8n79fcetrfgl926xfntmjxrfswtfs3dv5w2fcjy5scgcws9j2j8f
                 WitnessProgram:                 54f87c90f3f1538cac6947caad19335ee461a60e5a6116b28e5271225218461d
```
```
python mycryptowallet/wallet.py list addresses

Address 0: b'14ijPmxQSpez1AR6wLNGao77seV9gyBgiH'
Address 1: b'1NKm5vvjridBZVGTTsVkXRHS2yEunRSyxd'
Address 2: b'1QBkZibsYKf8fjhQHri57zWtq2V9XtmgLr'
```
```
python mycryptowallet/wallet.py delete address 1ArV16N7JfR86xxKaxZVwpc8HgDBdohDT1 1G3vKUrnYU4AyDuUj1CbmX8fzAA63MFeVm 1GDkrfpDjzKjrMU7ky2rQYNVCknDd9onx 1QD2bgC1cpGV8zSDWd4VwfiAPHvn9PfPMX
```
```
python mycryptowallet/wallet.py import address 5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny
> New address generated:
     Private key (raw hex):                      b'3e1258347b897fee4055b0ae9f59b459f31905815e9214bfddede6990f73b36f'
     Private key (WIF uncompressed format):      5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny
     Private key (WIF compressed format):        KyJNRBYQRJJDz2FPkc6ei5FaUerSt1JegV3o4vFxEt4P924VYdTn
     Public key (raw hex):                       0444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db0
     Public key (compressed format):             Kmo8qPN3sHiGata4QN9zx5Rda6H8ML2yRqXj42DtAgarfVYHMtprMSynLYQ6pQYjn4347xraQQe3GSEBQY2AugffKh
     Addresses by payment method:
         P2PKH (uncompressed):                   19LH6eahzaBVU9rz6TK81rUJ8ZfdyAsM3S
         P2PKH (compressed):                     16zL8KPTGraBuhHeQymiZmWcRrD92vBBNj
         P2SH:
             P2PKH:
                 Address:                        3Gttx49gcG8TKcApWVgH8bovDmEGp2zvZ3
                 RedeemSript:                    76a91441b04df087fcec32ea1900f38fda3c14520428ef88ac
             P2MULTISIG (one-of-one):
                 Address:                        3DiL5fRuXGSm6V6QgE227HRcxSqSJvGYrd
                 RedeemSript:                    51410444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db051ae
             P2WPKH:
                 Address:                        3K3utwxrfhcNvaVznLR261sWBdt3z4BMoF
                 WitnessProgram:                 001441b04df087fcec32ea1900f38fda3c14520428ef
         P2WPKH:                                 bc1qgxcymuy8lnkr96seqreclk3uz3fqg280rxgrr8
         P2WSH:
             P2PKH:
                 Address:                        bc1qjdfsfyjf6kf7pm3ud57scnr34jadlcfkn4720tmlydl9cetakfyqne26ah
                 WitnessProgram:                 9353049249d593e0ee3c6d3d0c4c71acbadfe1369d7ca7af7f237e5c657db248
             P2MULTISIG (one-of-one):
                 Address:                        bc1q2nu8ey8n79fcetrfgl926xfntmjxrfswtfs3dv5w2fcjy5scgcws9j2j8f
                 WitnessProgram:                 54f87c90f3f1538cac6947caad19335ee461a60e5a6116b28e5271225218461d
```
```
python wallet.py

wallet.py <action> <object>
     actions:
         create
         list
         delete
         import
   For more information use help in every action
```

Stay tuned for new formats and features!