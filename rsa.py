import random
from sympy import isprime

def generate_prime_number(n):
    while True:
        prime_number = random.randint(2**(n-1), 2**n)
        if isprime(prime_number):
            return prime_number

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        x2 = x1
        x1 = x
        
        d = y1
        
    if temp_phi == 1:
        return d + phi

def encrypt_rsa(message, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char),e,n) for char in message]
    return cipher_text

def main():
    p = generate_prime_number(1024)
    q = generate_prime_number(1024)
    
    n = p * q
    phi = (p-1) * (q-1)

    e = random.randint(1, phi)
    
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)

    public_key =(e,n)

    message_to_encrypt = input("Enter a message to encrypt: ")
    
    encrypted_msg = encrypt_rsa(message_to_encrypt, public_key)
    
    print(f"Encrypted message is: {encrypted_msg}")
    print(f"Values are p: {p}, q: {q}, and e: {e}")

if __name__ == "__main__":
    main()
