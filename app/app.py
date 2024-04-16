from flask import Flask, render_template
from extensions import app, db
from models import DB_result_text


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contacted')
def contacted():
    return render_template('contacted.html')

@app.route('/model')
def model():
    return render_template('model.html')


def create_tables(): #create all tables from models.py
    with app.app_context():
        db.create_all()

if __name__ == '__main__': 
    
    create_tables()
       
    app.run(debug=True, host='0.0.0.0')
    