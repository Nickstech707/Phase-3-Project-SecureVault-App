# app/auth.py
import sqlite3
from .models import Database, Encryption

class Auth:
    def __init__(self):
        self.db = Database()
        self.encryption = Encryption()

    def register(self, username, password):
        encrypted_password = self.encryption.encrypt(password)
        try:
            with self.db.connection:
                self.db.connection.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, encrypted_password))
            return True
        except sqlite3.IntegrityError:
            return False

    def login(self, username, password):
        cursor = self.db.connection.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            decrypted_password = self.encryption.decrypt(user[1])
            if decrypted_password == password:
                return user[0]
        return None