import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define SQLAlchemy instance
db = SQLAlchemy(app)