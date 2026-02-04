def test_request_without_api_key(client):
    response = client.get("/people/")
    assert response.status_code == 422 or response.status_code == 401


def test_request_with_invalid_api_key(client):
    response = client.get(
        "/people/",
        headers={"X-API-Key": "invalid-key"}
    )
    assert response.status_code == 401


def test_request_with_valid_api_key(client, auth_headers):
    response = client.get("/people/", headers=auth_headers)
    assert response.status_code == 200
