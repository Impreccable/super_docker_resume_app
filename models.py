#Import the base class from sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, TIMESTAMP, JSON
from sqlalchemy.dialects.mysql import VARCHAR

#Create a class Base
Base = declarative_base()

# Create table class that inherit the Base class
class submitted_text(Base):
    __tablename__ = "submitted_texts"
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP)
    real_text = Column(VARCHAR)
    real_text_length = Column(Integer)
    word_frequency = Column(JSON)

    def __init__(self, id, created_at, real_text, real_text_length, word_frequency):
        self.__user.id = id
        self.__user_created_at = created_at
        self.__user_real_text = real_text
        self.__user_real_text_length = real_text_length
        self.__user_word_frequency = word_frequency






#Create the tables in the db
#DATABASE_URI = "postgres+psycopg2://${POSTGRES_USER}:<${POSTGRES_PASSWORD}>@<postgresql_container>:5432/postgres"
DATABASE_URI = "postgres+psycopg2://postgres:Azerty123!!!@postgresql_container:5432/postgres"

from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
