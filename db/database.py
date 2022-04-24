from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = 'postgresql://kufkznhg:6LOhYbK5nSNUUqz1CrUUwofJr6tFBDGq@chunee.db.elephantsql.com/kufkznhg'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()