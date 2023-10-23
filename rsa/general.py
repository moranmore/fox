from Crypto.Util.number import *

def sol(n:int,p:int,c:int,e=65537):
    q = n//p
    d = inverse(e,(p-1)*(q-1))
    print("plain text:",long_to_bytes(pow(c,d,n)))

def common_module(e1:int,e2:int,n)