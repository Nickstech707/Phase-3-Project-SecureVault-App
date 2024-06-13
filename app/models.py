# app/models.py
import sqlite3
from cryptography.fernet import Fernet
import os

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.create_tables()

    def create_tables(self):
        with self.connection:
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )
            """)
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE
            )
            """)
            self.connection.execute("""
            CREATE TABLE IF NOT EXISTS credentials (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                website TEXT,
                username TEXT,
                password TEXT,
                category_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (category_id) REFERENCES categories (id)
            )
            """)

class Encryption:
    def __init__(self):
        self.key_file = 'encryption_key.key'
        self.key = self.load_key()
        self.cipher = Fernet(self.key)

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)
        return key

    def load_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()
        else:
            return self.generate_key()

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, token):
        return self.cipher.decrypt(token.encode()).decode()
