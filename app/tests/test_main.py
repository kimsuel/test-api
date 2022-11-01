from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

"""
test_root() : "root" API 함수에 대해 GET 방식으로 요청하여 테스트
test_read_item() : "read_item" API 함수에 대해 item_id가 1인 item을 params 값에 추가하여 GET 방식으로 테스트하는 함수
test_create_item() : "create_item" API 함수에 대해 생성할 item을 json값에 추가하여 POST 방식으로 요청하여 테스트하는 함수
"""

def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello World"}


def test_read_item():
    response = client.get('/items/foo', params={'item_id': '1'})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero"
    }


def test_create_item():
    response = client.post(
        '/items/',
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters"
    }