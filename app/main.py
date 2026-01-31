from fastapi import FastAPI
from app.routes import people, films, planets, starships

app = FastAPI(
    title="Star Wars API",
    description="API de consulta de dados do universo Star Wars",
    version="1.0.0",
)

app.include_router(people.router, prefix="/people", tags=["People"])
app.include_router(planets.router, prefix="/planets", tags=["Planets"])
app.include_router(films.router, prefix="/films", tags=["Films"])
app.include_router(starships.router, prefix="/starships", tags=["Starships"])


@app.get("/")
def health_check():
    return {"status": "ok"}
