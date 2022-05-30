from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:asterisk123@127.0.0.1/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLAlchemy(app)

app.register_blueprint(contacts)
