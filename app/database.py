echo from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User, Credential

engine = create_engine('sqlite:///password_manager.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    init_db()