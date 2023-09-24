from ecdsa import SigningKey, NIST384p

def encrypt_ecc(message):
    sk = SigningKey.generate(curve=NIST384p)
    vk = sk.get_verifying_key()
    signature = sk.sign(message.encode())
    return signature, vk

def main():
    message_to_encrypt = input("Enter a message to encrypt: ")
    
    encrypted_msg, vk = encrypt_ecc(message_to_encrypt)
    
    print(f"Encrypted message is: {encrypted_msg}")
    print(f"Verifying key is: {vk.to_string()}")

if __name__ == "__main__":
    main()
