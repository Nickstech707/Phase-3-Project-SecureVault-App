#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet


key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

Base = declarative_base()


def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher_suite = Fernet(key)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    credentials = relationship('Credential', backref='owner', lazy=True)

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)
    credentials = relationship('Credential', backref='category', lazy=True)

class Credential(Base):
    __tablename__ = 'credential'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    website = Column(String(150), nullable=False)
    username = Column(String(150), nullable=False)
    password = Column(String(256), nullable=False)

    @property
    def decrypted_password(self):
        return cipher_suite.decrypt(self.password.encode()).decode()

    @decrypted_password.setter
    def decrypted_password(self, plain_password):
        self.password = cipher_suite.encrypt(plain_password.encode()).decode()