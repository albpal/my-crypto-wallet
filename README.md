[![Build Status](http://37.247.52.181:8080/buildStatus/icon?job=mycryptowallet)](http://37.247.52.181:8080/job/mycryptowallet/)
# my-crypto-wallet
Simple wallet I'm building for learning purposes. To use it (Python 3.6 or higher):

```
python wallet.py create address

#### New address generated ####
     Private key (standard format):  f6fc7b120fc5f2a01550eebed7def18ecc999369ad66a42b16987a12005eaf21
     Public key (uncompress format): 047bf599045966fb5565f48506c1d1b999533ea9f1689146aaa357b594575394f2c0ab89c70426b27e04cb50c923451754c24c780d1f2d4d589a23046553b783c0
     Bitcoin address:                1nhD5prA9ueH2brnvrJ6k2ZfhrckbgrPD
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