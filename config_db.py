#Import the base class from sqlalchemy
from sqlalchemy.ext.declarative import declarative_base



DATABASE_URI = "postgres+psycopg2://${POSTGRES_USER}:<${POSTGRES_PASSWORD}>@<postgresql_container>:5432/postgres"

from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)
