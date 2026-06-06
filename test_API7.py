import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

# @pytest.fixture()
# def API_with_params():
#     response = requests.get(base_url, params={"userId":1})
#     return response
#
# def test_code_stat(API_with_params):
#     assert API_with_params.status_code == 200
#
# def test_post_count(API_with_params):
#     data = API_with_params.json()
#     assert len(data) == 10
#
#
# def test_all_posts_belong_to_user(API_with_params):
#     data = API_with_params.json()
#     for post in data:
#         assert post["userId"] == 1
#
# def test_data_is_exist(API_with_params):
#     data = API_with_params.json()
#     assert len(data) > 0
# #############################################################################

@pytest.mark.parametrize("post", [1, 2, 3])

def test_API_with_params(post):
    response = requests.get(base_url, params={"userId":post})
    data = response.json()


    assert response.status_code == 200
    assert len(data) == 10

    for num in data:
        assert num["userId"] == post

