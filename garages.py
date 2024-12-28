from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Garage(BaseModel):
    id: int
    name: str
    address: str

garages = [
    Garage(id=1, name="Garage One", address="123 Main St"),
    Garage(id=2, name="Garage Two", address="456 Elm St"),
]

@router.get("/", response_model=List[Garage])
def get_garages():
    return garages
