from unittest.mock import Mock, patch

from app.services.swapi_service import SwapiService


def make_response(json_data, status_code=200):
    mock = Mock()
    mock.status_code = status_code
    mock.json.return_value = json_data
    mock.raise_for_status = Mock()
    return mock


@patch("app.services.swapi_service.requests.get")
def test_fetch_all_pagination(mock_get):
    data1 = {"results": [{"name": "Luke"}], "next": "https://swapi.dev/api/people/?page=2"}
    data2 = {"results": [{"name": "Leia"}], "next": None}

    mock_get.side_effect = [make_response(data1), make_response(data2)]

    results = SwapiService.fetch_all("people")

    assert isinstance(results, list)
    assert len(results) == 2
    assert results[0]["name"] == "Luke"
    assert results[1]["name"] == "Leia"


@patch("app.services.swapi_service.requests.get")
def test_fetch_with_params(mock_get):
    expected = {"count": 1}
    mock_get.return_value = make_response(expected)

    params = {"search": "Luke"}
    resp = SwapiService.fetch("people", params=params)

    mock_get.assert_called_with("https://swapi.dev/api/people/", params=params)
    assert resp == expected


@patch("app.services.swapi_service.requests.get")
def test_fetch_by_url(mock_get):
    url = "https://swapi.dev/api/people/1/"
    expected = {"name": "Luke"}

    mock_get.return_value = make_response(expected, 200)

    resp = SwapiService.fetch_by_url(url)

    mock_get.assert_called_with(url)
    assert resp == expected


@patch("app.services.swapi_service.requests.get")
def test_fetch_by_url_returns_none_on_error(mock_get):
    url = "https://swapi.dev/api/people/1/"

    mock_get.return_value = make_response({}, 404)

    resp = SwapiService.fetch_by_url(url)

    assert resp is None
