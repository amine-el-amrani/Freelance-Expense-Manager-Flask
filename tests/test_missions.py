import pytest
from app import create_app, db
from app.models import Mission

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

def test_create_mission(client, token):
    response = client.post('/missions/', json={
        'name': 'Mission 1',
        'description': 'Description of mission 1'
    }, headers={'Authorization': f'Bearer {token}'})
    print(response.get_json())
    assert response.status_code == 201

def test_get_missions(client, token):
    response = client.post('/missions/', json={
        'name': 'Mission 1',
        'description': 'Description of mission 1'
    }, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201

    response = client.get('/missions/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    missions = response.get_json()
    print(missions)
    assert len(missions) == 1
    assert missions[0]['name'] == 'Mission 1'