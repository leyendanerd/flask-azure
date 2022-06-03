from routes.contacts import contacts
with contacts.test_client() as c:
    response = c.get('/')
    assert response.status_code == 200