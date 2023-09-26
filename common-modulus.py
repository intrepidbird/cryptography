from Crypto.Util.number import inverse, GCD

def common_modulus_attack(n, e1, e2, c1, c2):
    gcd, s1, s2 = GCD(e1, e2)

    # Ensure s1 is positive and s2 is negative
    if s1 < 0:
        s1, s2 = s2, s1
        c1, c2 = c2, c1

    inv_c2 = inverse(c2, n)
    m = (pow(c1, s1, n) * pow(inv_c2, -s2, n)) % n
    return m

# Example usage:
n = 3233  # Common modulus
e1 = 17   # Public exponent 1
e2 = 413  # Public exponent 2
c1 = 855  # Cipher text 1
c2 = 1809 # Cipher text 2

m = common_modulus_attack(n, e1, e2, c1, c2)
print("Decrypted message:", m)
