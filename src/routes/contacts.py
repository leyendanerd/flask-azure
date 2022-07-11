from crypt import methods
from flask import Blueprint, redirect, render_template, request, flash
from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)


@contacts.route('/')
def index():
    contacts = Contact.query.all()
    db.session.commit()

    return render_template('index.html', contacts=contacts)
    


@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()


    flash("Contacto fue agregado!")

    return redirect('/')


@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]
        db.session.commit()

        flash("Contacto fue actualizado!")

        return redirect('/')

    return render_template("update.html", contact=contact)


@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)

    flash("Contacto fue eliminado!")

    return redirect('/')


@contacts.route("/about")
def about():
    db.session.commit()
    return render_template('about.html')




