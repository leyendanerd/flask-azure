
from flask import Flask

app = Flask(__name__)

from routes.contacts import contacts
app.register_blueprint(contacts)

with app.test_client() as c:
    response = c.get('/')