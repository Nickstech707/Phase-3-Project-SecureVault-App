from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import session

class Auth:
    def register(self, username, password):
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        try:
            session.add(new_user)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            return False

    def login(self, username, password):
        user = session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user.id
        return None