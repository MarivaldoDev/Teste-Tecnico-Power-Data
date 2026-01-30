from fastapi import APIRouter, Query, HTTPException
from app.services.swapi_service import SwapiService

router = APIRouter()


@router.get("/")
def get_people(
    name: str | None = Query(None),
    gender: str | None = Query(None)
):
    people = SwapiService.fetch_all("people")

    if name:
        people = [
            p for p in people
            if name.lower() in p["name"].lower()
        ]

    if gender:
        people = [
            p for p in people
            if p["gender"] == gender
        ]

    return {
        "count": len(people),
        "results": people
    }


@router.get("/{person_id}/films")
def get_person_films(person_id: int):
    person = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/people/{person_id}/"
    )

    if not person:
        raise HTTPException(status_code=404, detail="Character not found")

    films_urls = person.get("films", [])

    films = []
    for url in films_urls:
        film = SwapiService.fetch_by_url(url)
        films.append({
            "title": film["title"],
            "episode_id": film["episode_id"],
            "release_date": film["release_date"]
        })

    return {
        "character": person["name"],
        "films_count": len(films),
        "films": films
    }


@router.get("/{person_id}/planet")
def get_person_planet(person_id: int):
    person = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/people/{person_id}/"
    )

    if not person:
        raise HTTPException(status_code=404, detail="Character not found")

    planet_url = person.get("homeworld")

    planet = SwapiService.fetch_by_url(planet_url)

    return {
        "character": person["name"],
        "planet": {
            "name": planet["name"],
            "climate": planet["climate"],
            "terrain": planet["terrain"]
        }
    }


@router.get("/{person_id}/starships")
def get_person_starships(person_id: int):
    person = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/people/{person_id}/"
    )

    if not person:
        raise HTTPException(status_code=404, detail="Character not found")

    starships_urls = person.get("starships", [])

    starships = []
    for url in starships_urls:
        ship = SwapiService.fetch_by_url(url)
        starships.append({
            "name": ship["name"],
            "model": ship["model"],
            "manufacturer": ship["manufacturer"]
        })

    return {
        "character": person["name"],
        "starships_count": len(starships),
        "starships": starships
    }
