from flask import Flask, render_template
from extensions import app, db

from models import *

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

def create_tables():
    with app.app_context():
        try:
            db.create_all()
            for table in db.metadata.tables.keys():
                print(f"Table '{table}' created successfully.")
        except Exception as e:
            print("An error occurred while creating tables:", e)

if __name__ == '__main__': 
    
    create_tables()
       
    app.run(debug=True, host='0.0.0.0')
    