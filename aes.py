from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(s):
    return s + ((16-len(s)%16) * '{')

def encrypt_aes(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(message).encode())
    encrypted_text_decimal = int.from_bytes(encrypted_text, byteorder='big')
    return encrypted_text_decimal

def main():
    key = get_random_bytes(16)
    message_to_encrypt = input("Enter a message to encrypt: ")
    
    encrypted_msg = encrypt_aes(message_to_encrypt, key)
    
    print(f"Encrypted message in decimal is: {encrypted_msg}")

if __name__ == "__main__":
    main()
