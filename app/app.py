from flask import render_template, request, render_template, redirect, url_for, request, jsonify
import requests
from extensions import app, db
from datetime import datetime
from models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            text = request.form['text']
            
            ip = request.remote_addr
            created_at = datetime.now()

            DB_Contact.insert_contact(created_at, ip, name, email, text, phone=None)
            
            return redirect(url_for('contacted'))
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('contact.html')

@app.route('/contacted')
def contacted():
    return render_template('contacted.html')


#@app.route('/model', methods=['GET', 'POST'])
#def model():
#   if request.method == 'POST':
 #       return request.form['submitted-text']
#
 #   return render_template('model.html')

def create_tables():
    with app.app_context():
        try:
            db.create_all()
            for table in db.metadata.tables.keys():
                print(f"Table '{table}' created successfully.")
        except Exception as e:
            print("An error occurred while creating tables:", e)

### api part
@app.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        input_text = request.form['input_text'] #its from model.html <div class="submission">
        hf_token = "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"

        response = requests.post('http://localhost:11434', json={'text': input_text}, headers={'Authorization': f'Bearer {hf_token}'})
        result = response.json()

        processed_text = result['output']

        return render_template('model.html', processed_text=processed_text)

    return render_template('model.html')

if __name__ == '__main__': 
    
    create_tables()
    
    app.run(debug=True, host='0.0.0.0')
    