from app import app
with app.test_client() as c:
    response = c.get('/')



