from fastapi import APIRouter, HTTPException
from app.services.swapi_service import SwapiService

router = APIRouter()


@router.get("/{starship_id}/pilots")
def get_starship_pilots(starship_id: int):
    starship = SwapiService.fetch_by_url(
        f"https://swapi.dev/api/starships/{starship_id}/"
    )

    if not starship:
        raise HTTPException(status_code=404, detail="Starship not found")

    pilots_urls = starship.get("pilots", [])

    pilots = []
    for url in pilots_urls:
        person = SwapiService.fetch_by_url(url)
        pilots.append({
            "name": person["name"],
            "gender": person["gender"],
            "birth_year": person["birth_year"]
        })

    return {
        "starship": starship["name"],
        "pilots_count": len(pilots),
        "pilots": pilots
    }
