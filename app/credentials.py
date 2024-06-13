# app/credentials.py
from .models import Database, Encryption

class Credentials:
    def __init__(self):
        self.db = Database()
        self.encryption = Encryption()

    def add_category(self, name):
        with self.db.connection:
            self.db.connection.execute("INSERT INTO categories (name) VALUES (?)", (name,))
        print("Category added.")

    def get_category_id(self, name):
        cursor = self.db.connection.execute("SELECT id FROM categories WHERE name = ?", (name,))
        category = cursor.fetchone()
        if category:
            return category[0]
        return None

    def add_credential(self, user_id, website, username, password, category_name):
        encrypted_password = self.encryption.encrypt(password)
        category_id = self.get_category_id(category_name)
        if not category_id:
            self.add_category(category_name)
            category_id = self.get_category_id(category_name)
        with self.db.connection:
            self.db.connection.execute("""
            INSERT INTO credentials (user_id, website, username, password, category_id) VALUES (?, ?, ?, ?, ?)
            """, (user_id, website, username, encrypted_password, category_id))

    def get_credential(self, user_id, website):
        cursor = self.db.connection.execute("""
        SELECT website, username, password, category_id FROM credentials WHERE user_id = ? AND website = ?
        """, (user_id, website))
        credential = cursor.fetchone()
        if credential:
            category_name = self.get_category_name(credential[3])
            return {
                'website': credential[0],
                'username': credential[1],
                'password': self.encryption.decrypt(credential[2]),
                'category': category_name
            }
        return None

    def update_credential(self, user_id, website, username, password, category_name):
        encrypted_password = self.encryption.encrypt(password)
        category_id = self.get_category_id(category_name)
        if not category_id:
            self.add_category(category_name)
            category_id = self.get_category_id(category_name)
        with self.db.connection:
            self.db.connection.execute("""
            UPDATE credentials SET username = ?, password = ?, category_id = ? WHERE user_id = ? AND website = ?
            """, (username, encrypted_password, category_id, user_id, website))

    def delete_credential(self, user_id, website):
        with self.db.connection:
            self.db.connection.execute("""
            DELETE FROM credentials WHERE user_id = ? AND website = ?
            """, (user_id, website))

    def list_credentials(self, user_id):
        cursor = self.db.connection.execute("""
        SELECT website, username, password, category_id FROM credentials WHERE user_id = ?
        """, (user_id,))
        credentials = cursor.fetchall()
        return [
            {
                'website': credential[0],
                'username': credential[1],
                'password': self.encryption.decrypt(credential[2]),
                'category': self.get_category_name(credential[3])
            } for credential in credentials
        ]

    def get_category_name(self, category_id):
        cursor = self.db.connection.execute("SELECT name FROM categories WHERE id = ?", (category_id,))
        category = cursor.fetchone()
        if category:
            return category[0]
        return None



