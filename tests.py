import requests
import json

def test_create_task():
    r = requests.post('http://localhost:8000/v1/tasks', json={"title": "My First Task"})
    assert isinstance(r.json()["id"], str)
    assert len(r.json()) == 1

def test_list_all_tasks():
    r = requests.get('http://localhost:8000/v1/tasks')
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) >= 1
    assert isinstance(r.json()["tasks"][0]["id"], str)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 3
