from fastapi import APIRouter, HTTPException
from app.services.swapi_service import SwapiService

router = APIRouter()


@router.get("/{planet_id}/residents")
def get_planet_residents(planet_id: int):
    planet = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/planets/{planet_id}/"
    )

    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")

    residents_urls = planet.get("residents", [])

    residents = []
    for url in residents_urls:
        person = SwapiService.fetch_by_url(url)
        residents.append({
            "name": person["name"],
            "gender": person["gender"],
            "birth_year": person["birth_year"]
        })

    return {
        "planet": planet["name"],
        "residents_count": len(residents),
        "residents": residents
    }
