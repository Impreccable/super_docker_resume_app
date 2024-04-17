from flask import render_template, request, redirect, url_for, jsonify
import requests
from extensions import app, db
from datetime import datetime
from models import *
import json

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

def create_tables():
    with app.app_context():
        try:
            db.create_all()
            for table in db.metadata.tables.keys():
                print(f"Table '{table}' created successfully.")
        except Exception as e:
            print("An error occurred while creating tables:", e)

### API part

@app.route('/model', methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        try:
            input_text = request.form['input_text']
            static_prompt = request.form['static_prompt']

            response = requests.post('http://ollama_container:11434/api/generate', json={
                "model": "llama2",
                "prompt": input_text
            })

            if response.status_code == 200:
                generated_text = json.loads(response.text).get('generated_text', 'Error: No generated text found')
            else:
                generated_text = f"Error: {response.status_code} - {response.text}"

            return render_template('model.html', processed_text=generated_text, static_prompt=static_prompt)
        except Exception as e:
            return f"An error occurred: {e}"

    elif request.method == 'GET':

        return render_template('model.html', processed_text='', static_prompt='Sumup the given text')
        
if __name__ == '__main__': 
    #create_tables()
    app.run(debug=True, host='0.0.0.0')
