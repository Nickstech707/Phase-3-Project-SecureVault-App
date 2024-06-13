from sqlalchemy import create_engine
from .models import Base
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

def initialize_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")