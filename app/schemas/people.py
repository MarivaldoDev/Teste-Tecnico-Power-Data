from pydantic import BaseModel
from typing import List


class PersonOut(BaseModel):
    name: str
    gender: str


class PeopleResponse(BaseModel):
    count: int
    results: List[PersonOut]