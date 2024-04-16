from extensions import db

class DB_Result_Text(db.Model):
    __tablename__ = 'result_text'

    id = db.Column(db.Integer, primary_key=True)
    generated_text = db.Column(db.String(), unique=True, nullable=False)
    generated_text_length = db.Column(db.Integer, nullable=False)
    word_frequency = db.Column(db.JSON, nullable=True)
    text_subject = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<DbResultText %r>' % self.generated_text
    
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

class DB_Submitted_Text(db.Model):
    __tablename__ = 'submitted_text'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.Timestamp(), unique=True, nullable=False)
    real_text = db.Column(db.String(), unique=True, nullable=False)
    real_text_length = db.Column(db.Integer, nullable=False)
    word_frequency = db.Column(db.JSON, nullable=True)
  
    def __repr__(self):
        return '<SubmittedText %r>' % self.real_text
    
    @classmethod
    def insert_data(cls, created_at, real_text, real_text_length, word_frequency):
        new_data = cls(
            created_at=created_at,
            real_text=real_text,
            real_text_length=real_text_length,
            word_frequency=word_frequency
        )
        db.session.add(new_data)
        db.session.commit()

class DB_Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    ip = db.Column(db.String())
    name = db.Column(db.String())
    email = db.Column(db.String())
    phone = db.Column(db.String())
    text = db.Column(db.String())

    def __init__(self, created_at, ip, name, email, text, phone=None):
        self.created_at = created_at
        self.ip = ip
        self.name = name
        self.email = email
        self.phone = phone
        self.text = text

    @classmethod
    def insert_contact(cls, created_at, ip, name, email, text, phone=None):
        new_contact = cls(created_at=created_at, ip=ip, name=name, email=email, phone=phone, text=text)
        db.session.add(new_contact)
        db.session.commit()

    @classmethod
    def get_contacts(cls):
        return cls.query.all()

class DB_Statistic(db.Model):
    __tablename__ = 'statistic'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String())
    asked_service_time = db.Column(db.DateTime())
    number_of_clicks = db.Column(db.Integer)

    def __init__(self, ip, asked_service_time, number_of_clicks):
        self.ip = ip
        self.asked_service_time = asked_service_time
        self.number_of_clicks = number_of_clicks

    @classmethod
    def insert_statistic(cls, ip, asked_service_time, number_of_clicks):
        new_statistic = cls(ip=ip, asked_service_time=asked_service_time, number_of_clicks=number_of_clicks)
        db.session.add(new_statistic)
        db.session.commit()

    @classmethod
    def get_statistics(cls):
        return cls.query.all()