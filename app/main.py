from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import people, films, planets, starships

app = FastAPI(
    title="Star Wars API",
    description="API de consulta de dados do universo Star Wars",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(people.router, prefix="/people", tags=["People"])
app.include_router(planets.router, prefix="/planets", tags=["Planets"])
app.include_router(films.router, prefix="/films", tags=["Films"])
app.include_router(starships.router, prefix="/starships", tags=["Starships"])


templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def health_check(request: Request):
    return templates.TemplateResponse("health.html", {"request": request})
