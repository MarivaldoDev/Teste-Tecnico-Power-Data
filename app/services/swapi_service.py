import requests
from app.core.logging import logger

BASE_URL = "https://swapi.dev/api"


class SwapiService:

    @staticmethod
    def fetch_all(resource: str) -> list:
        results = []
        url = f"{BASE_URL}/{resource}/"

        while url:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            results.extend(data.get("results", []))
            url = data.get("next")

        return results

    @staticmethod
    def fetch(resource: str, params: dict = None) -> dict:
        response = requests.get(f"{BASE_URL}/{resource}/", params=params)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def fetch_by_url(url: str) -> dict:
        logger.info(f"Obtendo dados da SWAPI: {url}")
        
        response = requests.get(url)

        if response.status_code != 200:
            logger.warning(
                f"Erro na SWAPI {response.status_code} para a URL {url}"
            )
            return None

        return response.json()
