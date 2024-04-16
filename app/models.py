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