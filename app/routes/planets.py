from fastapi import APIRouter, HTTPException, Query, Depends
from app.core.security import verify_api_key
from app.services.swapi_service import SwapiService

router = APIRouter(dependencies=[Depends(verify_api_key)])


@router.get("/{planet_id}/residents")
def get_planet_residents(
    planet_id: int,
    gender: str | None = Query(default=None, description="Filtrar por gênero")
):
    planet = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/planets/{planet_id}/"
    )

    if not planet:
        raise HTTPException(status_code=404, detail="Planet not found")

    residents = []
    for url in planet.get("residents", []):
        person = SwapiService.fetch_by_url(url)
        residents.append({
            "name": person["name"],
            "gender": person["gender"],
            "birth_year": person["birth_year"]
        })

    if gender:
        residents = [
            r for r in residents if r["gender"] == gender
        ]

    return {
        "planet": planet["name"],
        "residents": residents
    }

