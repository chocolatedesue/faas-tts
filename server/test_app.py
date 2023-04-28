from app import app

from fastapi.testclient import TestClient
import requests

client = TestClient(app)


res = [0, 24, 0, 27, 0, 40, 0, 26, 0, 22, 0, 42, 0, 38, 0, 22, 0, 40, 0, 34, 0, 15, 0, 1, 0, 42, 0, 15, 0, 41, 0, 35, 0, 15, 0, 40, 0, 30, 0, 18, 0, 30, 0, 15, 0, 11, 0, 2, 0]

def test_g2p():
    response = client.post(
        "/g2p",body={"cleanner_name": "english_cleaners", "symbols": ["[", "]", ","], "text": "hello world"})
    assert response.status_code == 200