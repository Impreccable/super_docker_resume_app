from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, TIMESTAMP
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP)
    ip = Column(String)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    text = Column(String)

# constructor
    def __init__(self, engine):
        self.engine = engine

    def insert_contact(self, created_at, ip,name, email, phone, text):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        contact = Contact(created_at=created_at, ip=ip, name=name,email=email, phone=phone, text=text)
        session.add(contact)
        session.commit()
        session.close()

    
    def get_contacts(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        contacts = session.query(Contact).all()
        session.close()
        return contacts


class Statistic(Base):
    __tablename__ = 'statistic'

    ip = Column(Integer)
    asked_service_time = Column(TIMESTAMP)
    number_of_clicks = Column(Integer)
    # constructor
    def __init__(self, engine):
        self.engine = engine

    def insert_statistic(self, ip, asked_service_time, number_of_clicks):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        statistic = Statistic(ip=ip, asked_service_time=asked_service_time, number_of_clicks=number_of_clicks)
        session.add(statistic)
        session.commit()
        session.close()

    def get_statistics(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        statistics = session.query(Statistic).all()
        session.close()
        return statistics


DATABASE_URI = "postgres+psycopg2://${POSTGRES_USER}:<${POSTGRES_PASSWORD}>@<postgresql_container>:5432/postgres"
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)