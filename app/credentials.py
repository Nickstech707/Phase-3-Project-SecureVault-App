from sqlalchemy.orm import Session
from .database import engine
from .models import Credential
from cryptography.fernet import Fernet

class Credentials:
    def __init__(self):
        self.session = Session(bind=engine)
        self.key = open('secret.key', 'rb').read()
        self.cipher = Fernet(self.key)

    def add_credential(self, user_id, website, username, password, category=None):
        encrypted_password = self.cipher.encrypt(password.encode()).decode()
        new_credential = Credential(user_id=user_id, website=website, username=username, password=encrypted_password, category=category)
        self.session.add(new_credential)
        self.session.commit()

    def get_credential(self, user_id, website):
        credential = self.session.query(Credential).filter_by(user_id=user_id, website=website).first()
        if credential:
            credential.password = self.cipher.decrypt(credential.password.encode()).decode()
        return credential

    def update_credential(self, user_id, website, username, password, category):
        credential = self.get_credential(user_id, website)
        if credential:
            credential.username = username
            credential.password = self.cipher.encrypt(password.encode()).decode()
            credential.category = category
            self.session.commit()

    def delete_credential(self, user_id, website):
        credential = self.get_credential(user_id, website)
        if credential:
            self.session.delete(credential)
            self.session.commit()

    def list_credentials(self, user_id):
        creds = self.session.query(Credential).filter_by(user_id=user_id).all()
        for cred in creds:
            cred.password = self.cipher.decrypt(cred.password.encode()).decode()
        return creds