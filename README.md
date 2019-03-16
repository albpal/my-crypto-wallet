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
python mycryptowallet/wallet.py create multisig 2 4 rng

Address 1:
     Private key: 5J1KL3zFCgGvDVHyssc7L7gCyLJGwZxiYHRcyCnTam7niUTWScL
     Public key: 04bb02aad88960b2b93c6b4a61b683966c3720e70ae7da71676129f441a095787e239b3e2ad9305f1011241d106fa0adabfb2eefe264b52a108051f324b01d4109


Address 2:
     Private key: 5JWqTWSTW6ARLsu2C3QktZhsGPJzY1MTtKJGbHmKqJxb2rWnVGq
     Public key: 0497647726c390d855b7d208c841bf4a250816998eb169b60eaf3b9f7e058f42c8b4f8c9b6e0a4206dcabbf1ba851f56eff6c746e378aa62bf8bf25da0a10b65af


Address 3:
     Private key: 5HtPmEeyk544Q1fjT5gMWnwDRhSN3r7U2HY4yNcJqyZpCsxBoT1
     Public key: 0460d434c9a71ec0eec0cf5905604a56c904d2cc4895e5d77292682be73cd2550224433462264a36e30d008f21daeb2d3ecf91fa6a87194ddaa00f9f926c3a9428


Address 4:
     Private key: 5JWKU6kpN5BZBqfDjquYgK4tBx6Uiybwwm37mDCvaYUpWyq7VcE
     Public key: 04db1a3d7d1fee4589d3bc5b7dcef196b8e3edaed72c6aa5678d4729db5ee08980b0631557444656a4bc375e57d7b927d7ea7d444e54342b23043e7b9278ec70b8

Bitcoin multisig address: 3HP4hd3TZk1tBJavrNr7ABvYZz2fynJqsG
Bitcoin multisig redeem script: 524104bb02aad88960b2b93c6b4a61b683966c3720e70ae7da71676129f441a095787e239b3e2ad9305f1011241d106fa0adabfb2eefe264b52a108051f324b01d4109410497647726c390d855b7d208c841bf4a250816998eb169b60eaf3b9f7e058f42c8b4f8c9b6e0a4206dcabbf1ba851f56eff6c746e378aa62bf8bf25da0a10b65af410460d434c9a71ec0eec0cf5905604a56c904d2cc4895e5d77292682be73cd2550224433462264a36e30d008f21daeb2d3ecf91fa6a87194ddaa00f9f926c3a94284104db1a3d7d1fee4589d3bc5b7dcef196b8e3edaed72c6aa5678d4729db5ee08980b0631557444656a4bc375e57d7b927d7ea7d444e54342b23043e7b9278ec70b854ae
```

```
python mycryptowallet/wallet.py create multisig 2 4 input
Insert random numbers for private key 1: 3 5  6  3  3  2  2  4  6  3  1  3  1  5  6  6  6  3 1
Insert random numbers for private key 2: 4 1  1  5  3  1  3  1  1  3  6  2  5  1  6  1  3  3 3
Insert random numbers for private key 3: 2 4  3  5  5  5  6  4  3  5  5  6  1  6  1  3  4  1 6
Insert random numbers for private key 4: 2 6  6  4  6  3  4  1  5  2  6  5  3  1  2  2  1  5 6

Address 1:
     Private key: 5KUzQukY52ESujifvPpVWX8z9Kr85L2FuLdwQRgYHQpyXYw1eaM
     Public key: 047e0191755970668a72ca433374f48b7b0730f5c7cefedfe69391069357d585ee612e65f46daf4b34952cdf9c399f8cbfebed0e25a53da525f2c0640b86cd7405


Address 2:
     Private key: 5JnoDL1opVmeBYwgTJUAY1NrsC59RHrwkKbLqreL4axSvburX95
     Public key: 043dd43ad6b5498b32717d35dd1310d302d45305884d7069acee3b08081bdbc4bf5cde6ec7019d2b020a5feb1f3bb9c4a275264c13a407347e6b051d30f2b16e3f


Address 3:
     Private key: 5Jdwp5njpfZTFtL1UjUxWtmsw2nN4pYExHGMkVrC1pU1JcDRsL1
     Public key: 040f61f2230039a5f4445527a144bbf0f1c0e1eabefad6106b7f73f7ff75e90303681c8ef0ce8fa5312ddddb8d50cd4ad5dd770fa829f2f94a25cc848a8f808c1a


Address 4:
     Private key: 5K3Mf2JZof6AhWFaiPwuJRF6nDv8fwjR21kB9HUkHxWL6FLnGBn
     Public key: 04a5cc79a7e1ae6ceed4b0284a1336d26eedc7352363a4b843bbe3d12065dfd6b8c9e6750369e5490467970d5f3ac423c2dac9e317e41157ecb6f76f6a0a6cf87b

Bitcoin multisig address: 39cPMchALRf6hQBuc8oAhA8Q9S8vgLGWzo
Bitcoin multisig redeem script: 5241047e0191755970668a72ca433374f48b7b0730f5c7cefedfe69391069357d585ee612e65f46daf4b34952cdf9c399f8cbfebed0e25a53da525f2c0640b86cd740541043dd43ad6b5498b32717d35dd1310d302d45305884d7069acee3b08081bdbc4bf5cde6ec7019d2b020a5feb1f3bb9c4a275264c13a407347e6b051d30f2b16e3f41040f61f2230039a5f4445527a144bbf0f1c0e1eabefad6106b7f73f7ff75e90303681c8ef0ce8fa5312ddddb8d50cd4ad5dd770fa829f2f94a25cc848a8f808c1a4104a5cc79a7e1ae6ceed4b0284a1336d26eedc7352363a4b843bbe3d12065dfd6b8c9e6750369e5490467970d5f3ac423c2dac9e317e41157ecb6f76f6a0a6cf87b54ae
```

```
python mycryptowallet/wallet.py create multisig 2 4 both
Insert random numbers for private key 1: 3 5  6  3  3  2  2  4  6  3  1  3  1  5  6  6  6  3 1
Insert random numbers for private key 2: 4 1  1  5  3  1  3  1  1  3  6  2  5  1  6  1  3  3 3
Insert random numbers for private key 3: 2 4  3  5  5  5  6  4  3  5  5  6  1  6  1  3  4  1 6
Insert random numbers for private key 4: 2 6  6  4  6  3  4  1  5  2  6  5  3  1  2  2  1  5 6

Address 1:
     Private key: 5HyUHF9i8FvZpLpV8rwhnavQfuLsZaDEvoTWkyo8UNzkjHBXiyp
     Public key: 04ae827830eda04bba2003fa3934962d136017d4fe5652429d7aba87922da9926f0812833bd75907d9cdc0f0106d3091421ce04fd6d4d1de2f14fc64c52e70b387


Address 2:
     Private key: 5JZd2PPQkke8QdNF5Je6wu91hPrC2ay82T4MycK9myEZkCKvC7F
     Public key: 04bb3f54674707996b3047b2588365d05f5ae3ddbf1cff716e12cdd7182e95d2d24b75e633033796724285ea06fc08e58f8d6e27a4c4706fd022c6a39a94e8460a


Address 3:
     Private key: 5Hs4wDiRqRtHoiEEA9ykH9UuAPx7TcYRrSPHS74sZJrcvoqoHpU
     Public key: 04d7b756c6fd480cb73cfe88cc6778e8416f76ca5cc76672cdd899f83b0ebaf07f29c81fdce78678d2a87b205da06b47c2d2c412e9c413785608424c232d14a9f7


Address 4:
     Private key: 5Kd3cZWt1MQs66WFQDs7pHdGoYf19nBKSP1MvCEPyFJsYF4toSf
     Public key: 042e0a645c3bdf1850db2a849fee04112bcd9051f080e48dc6b36dc8ccc6de13c3725682e0bccd544289cb58f8587aae54b7a38460753305ad201c24f8406723e0

Bitcoin multisig address: 34hUuDWi6mbViHJgfzQSrCoDxJaCpS7Xk7
Bitcoin multisig redeem script: 524104ae827830eda04bba2003fa3934962d136017d4fe5652429d7aba87922da9926f0812833bd75907d9cdc0f0106d3091421ce04fd6d4d1de2f14fc64c52e70b3874104bb3f54674707996b3047b2588365d05f5ae3ddbf1cff716e12cdd7182e95d2d24b75e633033796724285ea06fc08e58f8d6e27a4c4706fd022c6a39a94e8460a4104d7b756c6fd480cb73cfe88cc6778e8416f76ca5cc76672cdd899f83b0ebaf07f29c81fdce78678d2a87b205da06b47c2d2c412e9c413785608424c232d14a9f741042e0a645c3bdf1850db2a849fee04112bcd9051f080e48dc6b36dc8ccc6de13c3725682e0bccd544289cb58f8587aae54b7a38460753305ad201c24f8406723e054ae
```

```
python mycryptowallet/wallet.py create multisig 2 4 none
Insert public key 1: 04ae827830eda04bba2003fa3934962d136017d4fe5652429d7aba87922da9926f0812833bd75907d9cdc0f0106d3091421ce04fd6d4d1de2f14fc64c52e70b387
Insert public key 2: 04bb3f54674707996b3047b2588365d05f5ae3ddbf1cff716e12cdd7182e95d2d24b75e633033796724285ea06fc08e58f8d6e27a4c4706fd022c6a39a94e8460a
Insert public key 3: 04d7b756c6fd480cb73cfe88cc6778e8416f76ca5cc76672cdd899f83b0ebaf07f29c81fdce78678d2a87b205da06b47c2d2c412e9c413785608424c232d14a9f7
Insert public key 4: 042e0a645c3bdf1850db2a849fee04112bcd9051f080e48dc6b36dc8ccc6de13c3725682e0bccd544289cb58f8587aae54b7a38460753305ad201c24f8406723e0
Bitcoin multisig address: 34hUuDWi6mbViHJgfzQSrCoDxJaCpS7Xk7
Bitcoin multisig redeem script: 524104ae827830eda04bba2003fa3934962d136017d4fe5652429d7aba87922da9926f0812833bd75907d9cdc0f0106d3091421ce04fd6d4d1de2f14fc64c52e70b3874104bb3f54674707996b3047b2588365d05f5ae3ddbf1cff716e12cdd7182e95d2d24b75e633033796724285ea06fc08e58f8d6e27a4c4706fd022c6a39a94e8460a4104d7b756c6fd480cb73cfe88cc6778e8416f76ca5cc76672cdd899f83b0ebaf07f29c81fdce78678d2a87b205da06b47c2d2c412e9c413785608424c232d14a9f741042e0a645c3bdf1850db2a849fee04112bcd9051f080e48dc6b36dc8ccc6de13c3725682e0bccd544289cb58f8587aae54b7a38460753305ad201c24f8406723e054ae
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