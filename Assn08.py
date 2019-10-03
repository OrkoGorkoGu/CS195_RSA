import math
import random

# arbitrary list of prime numbers to choose from
primeList = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109
    , 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
]

def main():

    ## Get p and q, two large prime integers
    p = int(input("Enter a (large) prime number:\n"))
    q = int(input("Enter a different (large) prime number:\n"))

    # Get n
    n = p * q

    # Get b
    b = (p - 1)*(q - 1)

    # get keys
    key_public = getPublicKey(n,b)
    key_private = getPrivateKey(n, key_public[1], b)

    # Get plaintext from user
    msg = input("Enter your message here:\n")
    
    # Obtain Ciphertext (and output)
    c = getCipher(msg, key_private)
    print("Your ciphertext is %s"%c)
    print("Here is your public key to decode.\n", key_public)

    # Decode, as receiver would have to do
    p = getPlaintext(c, key_public)
    print(p)
    

def getPlaintext(c, key):
    p = pow(c, key[1], key[0])
    return p.to_bytes((p.bit_length() +7)//8, 'big').decode()

def getCipher(s, key):
    p = int.from_bytes(s.encode(), byteorder='big')
    return pow(p,key[1], key[0])

def isRelativePrime(a,b):
    return math.gcd(a,b)==1

def getPublicKey(n,b):
    # Get E
    while True:
        e = random.randint(0, len(primeList))
        if (isRelativePrime(b,e)):
            break
    
    # Return n and e
    return [n,e]

def getPrivateKey(n, E, b):
    # get D
    (x,D,y) = egcd(E, b)

    return [n,D]

def extend_euclid(E,b):
    return egcd(E, b)
    

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

if __name__=="__main__":
    main()