from sqlalchemy.orm import Session
from .database import engine
from .models import Credential

class Credentials:
    def __init__(self):
        self.session = Session(bind=engine)

    def add_credential(self, user_id, website, username, password, category=None):
        new_credential = Credential(user_id=user_id, website=website, username=username, password=password, category=category)
        self.session.add(new_credential)
        self.session.commit()

    def get_credential(self, user_id, website):
        return self.session.query(Credential).filter_by(user_id=user_id, website=website).first()

    def update_credential(self, user_id, website, username, password, category):
        credential = self.get_credential(user_id, website)
        if credential:
            credential.username = username
            credential.password = password
            credential.category = category
            self.session.commit()

    def delete_credential(self, user_id, website):
        credential = self.get_credential(user_id, website)
        if credential:
            self.session.delete(credential)
            self.session.commit()

    def list_credentials(self, user_id):
        return self.session.query(Credential).filter_by(user_id=user_id).all()