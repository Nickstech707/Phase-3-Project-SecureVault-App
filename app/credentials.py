from .models import Credential, Category
from . import session
from sqlalchemy.exc import SQLAlchemyError

class Credentials:
    def add_credential(self, user_id, website, username, password, category_name=None):
        category = None
        if category_name:
            category = session.query(Category).filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                session.add(category)
                session.commit()
        new_credential = Credential(user_id=user_id, website=website, username=username, category_id=category.id if category else None)
        new_credential.decrypted_password = password
        try:
            session.add(new_credential)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    def get_credential(self, user_id, website):
        credential = session.query(Credential).filter_by(user_id=user_id, website=website).first()
        if credential:
            return {
                'website': credential.website,
                'username': credential.username,
                'password': credential.decrypted_password,
                'category': credential.category.name if credential.category else None
            }
        return None

    def update_credential(self, user_id, website, username, password, category_name=None):
        credential = session.query(Credential).filter_by(user_id=user_id, website=website).first()
        if credential:
            category = None
            if category_name:
                category = session.query(Category).filter_by(name=category_name).first()
                if not category:
                    category = Category(name=category_name)
                    session.add(category)
                    session.commit()
            credential.username = username
            credential.decrypted_password = password
            credential.category_id = category.id if category else None
            try:
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def delete_credential(self, user_id, website):
        credential = session.query(Credential).filter_by(user_id=user_id, website=website).first()
        if credential:
            try:
                session.delete(credential)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e

    def list_credentials(self, user_id):
        credentials = session.query(Credential).filter_by(user_id=user_id).all()
        return [
            {
                'website': credential.website,
                'username': credential.username,
                'password': credential.decrypted_password,
                'category': credential.category.name if credential.category else None
            }
            for credential in credentials
        ]