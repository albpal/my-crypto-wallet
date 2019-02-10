import hashlib

def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d

def hash160(x):
    return ripemd160(hashlib.sha256(x).digest())

def sha256(x):
    return hashlib.sha256(x)

def doubleSHA256(x):
    return hashlib.sha256(hashlib.sha256(x).digest())