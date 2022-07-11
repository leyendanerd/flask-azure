import os
import sentry_sdk
from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION 
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://0638fb48cd26422c8af88c268b0a8b85@o1275124.ingest.sentry.io/6523802",
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)

app = Flask(__name__)

app.secret_key = "Asterisk.123"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_MAX_OVERFLOW'] = -1

SQLAlchemy(app)

app.register_blueprint(contacts)
