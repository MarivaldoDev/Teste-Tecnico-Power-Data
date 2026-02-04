from fastapi import APIRouter, Query, HTTPException, Depends
from app.services.swapi_service import SwapiService
from app.core.security import verify_api_key
from app.schemas.people import PeopleResponse
from app.core.logging import logger

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.get("/", response_model=PeopleResponse)
def get_people(
    name: str | None = Query(None),
    gender: str | None = Query(None)
):
    logger.info("GET /people called")
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
def get_person_films(
    person_id: int,
    sort: str | None = Query(default=None, description="Campo para ordenação")
):
    
    logger.info(f"Obtendo filmes para person_id={person_id}")
    person = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/people/{person_id}/"
    )

    if not person:
        raise HTTPException(status_code=404, detail="Character not found")

    films = []
    for url in person.get("films", []):
        film = SwapiService.fetch_by_url(url)
        if film:
            films.append({
                "title": film["title"],
                "episode_id": film["episode_id"],
                "release_date": film["release_date"]
            })

    if sort and films and sort in films[0]:
        films.sort(key=lambda x: x[sort])

    return {
        "character": person["name"],
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

    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")

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
        if ship:
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