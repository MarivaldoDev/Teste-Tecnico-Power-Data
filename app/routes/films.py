from fastapi import APIRouter, Query, HTTPException
from app.services.swapi_service import SwapiService

router = APIRouter()


@router.get("/")
def get_films(
    title: str | None = Query(None, description="Filtrar por título"),
    director: str | None = Query(None, description="Filtrar por diretor")
):
    films = SwapiService.fetch_all("films")

    if title:
        films = [
            f for f in films
            if title.lower() in f["title"].lower()
        ]

    if director:
        films = [
            f for f in films
            if director.lower() in f["director"].lower()
        ]

    return {
        "count": len(films),
        "results": films
    }


@router.get("/{film_id}/characters")
def get_film_characters(film_id: int):
    film = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/films/{film_id}/"
    )

    if not film:
        raise HTTPException(status_code=404, detail="Film not found")

    characters_urls = film.get("characters", [])

    characters = []
    for url in characters_urls:
        character = SwapiService.fetch_by_url(url)
        characters.append({
            "name": character["name"],
            "gender": character["gender"],
            "birth_year": character["birth_year"]
        })

    return {
        "film": film["title"],
        "characters_count": len(characters),
        "characters": characters
    }