[![Build Status](http://37.247.52.181:8080/buildStatus/icon?job=mycryptowallet)](http://37.247.52.181:8080/job/mycryptowallet/)
# my-crypto-wallet
Simple wallet I'm building for learning purposes. To use it (Python 3.6 or higher):

```
python wallet.py create address

> New address generated (raws are binary, the others are in base58 encoded):
     Private key (raw):                        22ba635095c52fbbc2500177c6b10c3983b6e8e2dcb494a2f02a84d14869eec8
     Private key (WIF uncompressed format):    5J5afSmhC7nBcKBGp4Up6Tc9QMNFwri3m8LQqSW8x5xJ2KGRj6q
     Private key (WIF compressed format):      KxPDagkGQ4vRpsELniMks6S864tpy8QBBmNgCoZc68s48TKY1xfa
     Public key (raw):                         04640b8f007173b2f768a18fdc9d02f53dc0af3a99cb1476bcb2ac8b47ca42c1231b742869c9a44aabccadb571ae3d5e7a3a9c2f13498b06e3adf3ef3c7ff4e01f
     Public key (compressed format):           21RV73LHam3MfQcLbzy9ueocFhgzPXeXQasDyWCsSDiZp
     Bitcoin address:                          1KwQm2hSv3o6TwpNP1H32HTjMRcH2KdKmA
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
python wallet.py

wallet.py <action> <object>
     actions:
         create
         list
         delete
   For more information use help in every action
```

Stay tuned for new formats and features!