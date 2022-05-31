from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Asterisk123@0.0.0.0/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contacts)
