from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_home():
    reponse = client.get('/')
    assert reponse.status_code == 200
    assert 'text/html' in reponse.headers['content-type']

def test_post_home():
    reponse = client.post('/')
    assert reponse.status_code == 200
    assert 'application/json' in reponse.headers['content-type']
