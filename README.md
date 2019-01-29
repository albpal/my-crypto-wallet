[![Build Status](http://37.247.52.181:8080/buildStatus/icon?job=mycryptowallet)](http://37.247.52.181:8080/job/mycryptowallet/)
# my-crypto-wallet
Simple wallet I'm building for learning purposes. To use it (Python 3.6 or higher):

```
python mycryptowallet/wallet.py create address

 > New address generated (raws are binary, the others are in base58 encoded):
     Private key (raw):                        3e1258347b897fee4055b0ae9f59b459f31905815e9214bfddede6990f73b36f
     Private key (WIF uncompressed format):    5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny
     Private key (WIF compressed format):      KyJNRBYQRJJDz2FPkc6ei5FaUerSt1JegV3o4vFxEt4P924VYdTn
     Public key (raw):                         0444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db0
     Public key (compressed format):           g3SrTQLgheE7ZPhTjtLw4iQnakzzE3xPuzE7q3Hofpro
     Bitcoin address:                          19LH6eahzaBVU9rz6TK81rUJ8ZfdyAsM3S
     Bitcoin P2SH address:                     3K3utwxrfhcNvaVznLR261sWBdt3z4BMoF
     Bitcoin redeem script:                    001441b04df087fcec32ea1900f38fda3c14520428ef
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

 > New address generated (raws are binary, the others are in base58 encoded):
     Private key (raw):                        3e1258347b897fee4055b0ae9f59b459f31905815e9214bfddede6990f73b36f
     Private key (WIF uncompressed format):    5JHd7qcD6xaMcaMw6MBo9rSxciewMAauVRw6uYYwCkjubXsNUny
     Private key (WIF compressed format):      KyJNRBYQRJJDz2FPkc6ei5FaUerSt1JegV3o4vFxEt4P924VYdTn
     Public key (raw):                         0444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db0
     Public key (compressed format):           g3SrTQLgheE7ZPhTjtLw4iQnakzzE3xPuzE7q3Hofpro
     Bitcoin address:                          19LH6eahzaBVU9rz6TK81rUJ8ZfdyAsM3S
     Bitcoin P2SH address:                     3K3utwxrfhcNvaVznLR261sWBdt3z4BMoF
     Bitcoin redeem script:                    001441b04df087fcec32ea1900f38fda3c14520428ef
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