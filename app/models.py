from extensions import db

class DB_result_text(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    generated_text = db.Column(db.String(), unique=True, nullable=False)
    generated_text_length = db.Column(db.Integer, nullable=False)
    word_frequency = db.Column(db.JSON, nullable=True)
    text_subject = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<DB_result_text %r>' % self.generated_text
    
    @classmethod
    def insert_data(cls, generated_text, generated_text_length, word_frequency, text_subject):
        new_data = cls(
            generated_text=generated_text,
            generated_text_length=generated_text_length,
            word_frequency=word_frequency,
            text_subject=text_subject
        )
        db.session.add(new_data)
        db.session.commit()
        
class Contact(db.Model):
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


class Statistic(db.Model):
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

