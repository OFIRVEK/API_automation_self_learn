import pytest
import requests


POST_URL = "https://dummyjson.com/users/add"
GET_URL = "https://dummyjson.com/users"
payload = {
    "firstName": "Ofir",
    "lastName": "Test",
    "email": "ofir@test.com",
    "age": 30
}
@pytest.fixture()

def create_user():
    response_post = requests.post(POST_URL, json=payload)
    new_user_id = response_post.json()["id"]

    yield new_user_id, response_post

    requests.delete(f'{GET_URL}/{new_user_id}')


def test_data_creation(create_user):
    new_user_id,response_post = create_user
    response_get = requests.get(f'{GET_URL}/{new_user_id}')

    assert response_post.status_code == 201
    if response_get.status_code == 404:
        pytest.xfail("DummyJSON doesn't persist created users")
    assert response_get.status_code == 200


def test_user_deleted(create_user):
    new_user_id, _ = create_user

    # delete
    requests.delete(f"{GET_URL}/{new_user_id}")


    # verify it's gone
    response_get = requests.get(f'{GET_URL}/{new_user_id}')
    assert response_get.status_code == 404  # ← this is a validation
