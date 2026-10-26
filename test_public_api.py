"""Part 2: tests against JSONPlaceholder, a public API.

Complete API_FINDINGS.md before writing any test in this file. Each
assertion below should state what you recorded there, not a value
copied from the documentation.

Run with:
    pytest test_public_api.py -v
"""
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post():
    """GET /posts/1.

    Assert the status code, the Content-Type header, and that the
    response body contains the keys recorded in API_FINDINGS.md, each
    of the correct type.
    """
    
    response = requests.get(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    body = response.json()

    assert isinstance(body, dict)
    assert isinstance(body["userId"], int)
    assert isinstance(body["id"], int)
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)



def test_get_all_posts():
    """GET /posts.

    Assert the status code, the Content-Type header, and that the
    response body has the shape recorded in API_FINDINGS.md.
    """
    
    response = requests.get(
        f"{BASE_URL}/posts"
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    body = response.json()

    assert isinstance(body, list)
    assert len(body) == 100

    for post in body:
        assert isinstance(post, dict)
        assert isinstance(post["userId"], int)
        assert isinstance(post["id"], int)
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)



def test_create_post():
    """POST /posts.

    Send the request body recorded in API_FINDINGS.md. Assert the
    status code, the Content-Type header, and that the response body
    contains the fields you sent, plus the field the server adds.
    """
    
    payload = {
        "title": "Lab 6 API Test",
        "body": "Testing POST request",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    body = response.json()

    assert body["title"] == "Lab 6 API Test"
    assert body["body"] == "Testing POST request"
    assert body["userId"] == 1
    assert body["id"] == 101



def test_delete_post():
    """DELETE /posts/1.

    Assert the status code and the Content-Type header recorded in
    API_FINDINGS.md.
    """
    
    response = requests.delete(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    body = response.json()
    assert body == {}

