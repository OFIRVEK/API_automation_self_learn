import pytest
import requests



payload = { "title": 'Chain Test', "body": 'Testing chains', "userId": 1 }
base_url = "https://jsonplaceholder.typicode.com/posts"
@pytest.fixture()
def chained_API_test():
    response_post = requests.post(base_url, json=payload)
    post_id = response_post.json()["id"]
    response_get  = requests.get(f"{base_url}/{post_id}")
    print(response_get.status_code)
    print(response_get.json())
    return response_post,response_get


@pytest.mark.xfail(reason="JSONPlaceholder doesn't actually save POSTed data")

def test_assertions(chained_API_test):
    response_post, response_get = chained_API_test
    assert response_get.json()["id"] == response_post.json()["id"]
    assert response_post.status_code == 201
    assert response_get.status_code == 200


