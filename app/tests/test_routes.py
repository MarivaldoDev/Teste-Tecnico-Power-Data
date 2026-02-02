from unittest.mock import patch


@patch("app.services.swapi_service.SwapiService.fetch_all")
def test_get_films_filter_and_count(mock_fetch, client, auth_headers):
    mock_fetch.return_value = [
        {"title": "A New Hope", "director": "George Lucas"},
        {"title": "Return of the Jedi", "director": "Richard Marquand"},
    ]

    response = client.get("/films/?title=hope&director=George Lucas", headers=auth_headers)

    assert response.status_code == 200
    body = response.json()
    assert body["count"] == 1


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_film_characters_success(mock_fetch, client, auth_headers):
    film = {"title": "A New Hope", "characters": ["u1", "u2"]}
    c1 = {"name": "Luke", "gender": "male", "birth_year": "19BBY"}
    c2 = {"name": "Leia", "gender": "female", "birth_year": "19BBY"}

    def side(url):
        if "films" in url:
            return film
        if url == "u1":
            return c1
        return c2

    mock_fetch.side_effect = side

    response = client.get("/films/1/characters", headers=auth_headers)

    assert response.status_code == 200
    body = response.json()
    assert body["film"] == "A New Hope"
    assert body["characters_count"] == 2


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_film_characters_404(mock_fetch, client, auth_headers):
    mock_fetch.return_value = None

    response = client.get("/films/999/characters", headers=auth_headers)

    assert response.status_code == 404


@patch("app.services.swapi_service.SwapiService.fetch_all")
def test_get_people_filters(mock_fetch, client, auth_headers):
    mock_fetch.return_value = [
        {"name": "Luke Skywalker", "gender": "male"},
        {"name": "Leia Organa", "gender": "female"},
    ]

    response = client.get("/people/?name=Luke&gender=male", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["count"] == 1


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_person_films_returns_404_when_person_not_found(mock_fetch, client, auth_headers):
    mock_fetch.return_value = []

    response = client.get("/people/999/films", headers=auth_headers)

    assert response.status_code == 404



@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_person_films_sort(mock_fetch, client, auth_headers):
    def side(url):
        if "people" in url:
            return {"name": "Luke", "films": ["f1", "f2"]}
        if "f1" in url:
            return {"title": "B", "episode_id": 2, "release_date": "1980-05-21"}
        return {"title": "A", "episode_id": 1, "release_date": "1977-05-25"}

    mock_fetch.side_effect = side

    response = client.get("/people/1/films?sort=episode_id", headers=auth_headers)

    assert response.status_code == 200
    films = response.json()["films"]
    assert films[0]["episode_id"] == 1


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_person_planet_success_and_not_found(mock_fetch, client, auth_headers):
    def side(url):
        if "people" in url:
            return {"name": "Luke", "homeworld": "planet_url"}
        if url == "planet_url":
            return {"name": "Tatooine", "climate": "arid", "terrain": "desert"}
        return None

    mock_fetch.side_effect = side

    response = client.get("/people/1/planet", headers=auth_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["planet"]["name"] == "Tatooine"

    def side2(url):
        if "people" in url:
            return {"name": "Luke", "homeworld": "planet_url"}
        return None

    mock_fetch.side_effect = side2
    response2 = client.get("/people/1/planet", headers=auth_headers)
    assert response2.status_code == 404


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_person_starships(mock_fetch, client, auth_headers):
    def side(url):
        if "people" in url:
            return {"name": "Luke", "starships": ["s1"]}
        if url == "s1":
            return {"name": "X-Wing", "model": "T-65", "manufacturer": "Incom"}
        return None

    mock_fetch.side_effect = side

    response = client.get("/people/1/starships", headers=auth_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["starships_count"] == 1


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_planet_residents_and_gender_filter(mock_fetch, client, auth_headers):
    planet = {"name": "Alderaan", "residents": ["r1", "r2"]}
    r1 = {"name": "Person1", "gender": "male", "birth_year": "100BBY"}
    r2 = {"name": "Person2", "gender": "female", "birth_year": "101BBY"}

    def side(url):
        if "planets" in url:
            return planet
        if url == "r1":
            return r1
        return r2

    mock_fetch.side_effect = side

    response = client.get("/planets/1/residents", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["planet"] == "Alderaan"

    response2 = client.get("/planets/1/residents?gender=female", headers=auth_headers)
    assert response2.status_code == 200
    assert len(response2.json()["residents"]) == 1


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_planet_residents_returns_404_when_planet_not_found(mock_fetch, client, auth_headers):
    mock_fetch.return_value = None
    response = client.get("/planets/999/residents", headers=auth_headers)
    assert response.status_code == 404


@patch("app.services.swapi_service.SwapiService.fetch_by_url")
def test_get_starship_pilots_success_and_404(mock_fetch, client, auth_headers):
    ship = {"name": "Falcon", "pilots": ["p1"]}
    p1 = {"name": "Han", "gender": "male", "birth_year": "29BBY"}

    def side(url):
        if "starships" in url:
            return ship
        if url == "p1":
            return p1
        return None

    mock_fetch.side_effect = side

    response = client.get("/starships/10/pilots", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["pilots_count"] == 1

    mock_fetch.side_effect = lambda url: None
    response2 = client.get("/starships/999/pilots", headers=auth_headers)
    assert response2.status_code == 404
