import pytest
from app import create_app, db
from app.models import User, Mission, Expense

@pytest.fixture
def app():
    app = create_app('config.TestingConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def token(client):
    client.post('/auth/register', json={
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword'
    })
    response = client.post('/auth/login', json={
        'email': 'test@example.com',
        'password': 'testpassword'
    })
    return response.get_json()['token']

def test_create_expense(client, token):
    client.post('/missions/', json={
        'name': 'Mission 1',
        'description': 'Description of mission 1'
    }, headers={'Authorization': f'Bearer {token}'})

    response = client.post('/expenses/', json={
        'amount': 100.0,
        'description': 'Expense 1',
        'date': '2024-07-18',
        'mission_id': 1
    }, headers={'Authorization': f'Bearer {token}'})
    print(response.get_json())  # Ajoute ceci pour imprimer la réponse
    assert response.status_code == 201

def test_get_expenses(client, token):
    client.post('/missions/', json={
        'name': 'Mission 1',
        'description': 'Description of mission 1'
    }, headers={'Authorization': f'Bearer {token}'})

    client.post('/expenses/', json={
        'amount': 100.0,
        'description': 'Expense 1',
        'date': '2024-07-18',
        'mission_id': 1
    }, headers={'Authorization': f'Bearer {token}'})

    response = client.get('/expenses/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    expenses = response.get_json()
    print(expenses)
    assert len(expenses) == 1
    assert expenses[0]['description'] == 'Expense 1'
