from unittest.mock import patch

@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_person_films(mock_fetch, client, auth_headers):
    def side_effect(url):
        if "people" in url:
            return {
                "name": "Luke Skywalker",
                "films": ["film1"]
            }
        return {
            "title": "A New Hope",
            "episode_id": 4,
            "release_date": "1977-05-25"
        }

    mock_fetch.side_effect = side_effect

    response = client.get("/people/1/films", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["character"] == "Luke Skywalker"
