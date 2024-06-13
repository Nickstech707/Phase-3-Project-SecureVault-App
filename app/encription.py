from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher_suite = Fernet(key)

def encrypt(text):
    return cipher_suite.encrypt(text.encode()).decode()

def decrypt(encrypted_text):
    return cipher_suite.decrypt(encrypted_text.encode()).decode()