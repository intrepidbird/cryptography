from Crypto.PublicKey import RSA

def generate_rsa_keys(bitsize):
    key = RSA.generate(bitsize)
    public_key = key.publickey().exportKey("PEM")
    private_key = key.exportKey("PEM")
    return public_key, private_key

bitsize = 1024  # Replace with desired bit size
public_key, private_key = generate_rsa_keys(bitsize)

print("Public Key:", public_key)
print("Private Key:", private_key)
