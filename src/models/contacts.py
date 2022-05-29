from utils.db import db


class Contact(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    fullname = db.Colum(db.String(80))
    email = db.Colum(db.String(100))
    phone = db.Colum(db.String(100))

    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone
