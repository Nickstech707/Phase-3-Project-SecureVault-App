echo from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import Session
from .database import engine
from .models import User

class Auth:
    def __init__(self):
        self.session = Session(bind=engine)

    def register(self, username, password):
        if self.session.query(User).filter_by(username=username).first():
            return False
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(username=username, password=hashed_password)
        self.session.add(new_user)
        self.session.commit()
        return True

    def login(self, username, password):
        user = self.session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user.id
        return None