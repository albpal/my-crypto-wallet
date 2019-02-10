[![Build Status](http://37.247.52.181:8080/buildStatus/icon?job=mycryptowallet)](http://37.247.52.181:8080/job/mycryptowallet/)
# my-crypto-wallet
Simple wallet I'm building for learning purposes. To use it (Python 3.6 or higher):

```
python mycryptowallet/wallet.py create address

 > New address generated:
     Private key (raw hex):                      b'9d7697f514812c0b9635dac3396b5b104ea4090c9013c5243304618fa759bcf1'
     Private key (WIF uncompressed format):      5K1dmZLdP1pvmk56neqsL2PL8xX4meS3WKHbAvUJjn7xAwYbvE6
     Private key (WIF compressed format):        L2VoHfjdaAeYLV76YW2h8y7ZU83he4DY4PiDpo1XHp9gWihNxYAN
     Public key (raw hex):                       0417bf93ea87cabd4de4b6e5bcf262036dcb7cb4c5f500267d30fa578072f05b195f90c297ad70cd3a7b18f795eb4757d461bbfbf8de6e1ca49f38e4178fe5c072
     Public key (compressed format):             Kmo5NTGEYrRuVfY8XHGBLesQwvB8mdB35uduq4ooh5awHvTy1YKecQ2vJHm2HtKgPqGgmAbzF4ZdBqPsuRi7Au8r2c
     Addresses by payment method:
         P2PK (uncompressed):                    14BfEAebwcPhX3kBgadpBf4sC1WaQb4hPe
         P2PK (compressed):                      14Whkj2A1KovDknyVSrybmGpYL7x6DiK8w
         P2SH-P2PKH:
             Address:                            3NM9Lz2ZrxjLxuk1U73NPDpU4AMWh7FDxS
             RedeemSript:                        76a914268675b97324b6cede9587a32bbfb03d106cd13f88ac
         P2SH-P2MULTISIG:
             Address:                            3QFhGAtL58uQxo8Cb2hoGxadarpDCfhnCq
             RedeemSript:                        51410417bf93ea87cabd4de4b6e5bcf262036dcb7cb4c5f500267d30fa578072f05b195f90c297ad70cd3a7b18f795eb4757d461bbfbf8de6e1ca49f38e4178fe5c07251ae
         P2SH-P2WPKH:
             Address:                            3AwcwBBvMRtjChXinjsmjKDvAgd9biSeWk
             WitnessProgram:                     0014268675b97324b6cede9587a32bbfb03d106cd13f
         P2SH-P2WPSH:
             Address:                            38GoMKSCgDGLaJ3wD26ZfuJzCNvFPm553e
             WitnessProgram:                     0020a3fd8cedf2aa33bc7a0f3ab562a0cf1ef8c482e67bd4284f0f4db5a5bdd79fd7
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
         P2PK (uncompressed):                    19LH6eahzaBVU9rz6TK81rUJ8ZfdyAsM3S
         P2PK (compressed):                      16zL8KPTGraBuhHeQymiZmWcRrD92vBBNj
         P2SH-P2PKH:
             Address:                            3Gttx49gcG8TKcApWVgH8bovDmEGp2zvZ3
             RedeemSript:                        76a91441b04df087fcec32ea1900f38fda3c14520428ef88ac
         P2SH-P2MULTISIG:
             Address:                            3DiL5fRuXGSm6V6QgE227HRcxSqSJvGYrd
             RedeemSript:                        51410444182ef73b3ed004308d41466776b00faaf6104760627490850b94af2c84aa3443266b8cd611d6205c20f809fdf390340873a8160638955a9504c65a46922db051ae
         P2SH-P2WPKH:
             Address:                            3K3utwxrfhcNvaVznLR261sWBdt3z4BMoF
             WitnessProgram:                     001441b04df087fcec32ea1900f38fda3c14520428ef
         P2SH-P2WPSH:
             Address:                            3HX1Hb5we9frxg8iSr4jEi66HZpUinPEZM
             WitnessProgram:                     00202cff2479d21c9f68f451dd7cce6dc62dd6cabc440fb14883c4ae71f26325aa02
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