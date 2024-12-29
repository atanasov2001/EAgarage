from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Garage(BaseModel):
    id: int
    name: str
    address: str
    capacity: int

garages = [
    Garage(id=1, name="Main Garage", address="123 Main St", capacity=50),
    Garage(id=2, name="East Garage", address="456 East St", capacity=30),
]

@router.post("/")
def create_garage(garage: Garage):
    garages.append(garage)
    return {"message": "Garage created successfully", "garage": garage}


@router.get("/", response_model=List[Garage])
def get_all_garages():
    return garages

@router.get("/{garage_id}", response_model=Garage)
def get_garage(garage_id: int):
    for garage in garages:
        if garage.id == garage_id:
            return garage
    return {"error": "Garage not found"}


@router.put("/{garage_id}")
def update_garage(garage_id: int, updated_garage: Garage):
    for index, garage in enumerate(garages):
        if garage.id == garage_id:
            garages[index] = updated_garage
            return {"message": "Garage updated successfully", "garage": updated_garage}
    return {"error": "Garage not found"}


@router.delete("/{garage_id}")
def delete_garage(garage_id: int):
    global garages
    garages = [garage for garage in garages if garage.id != garage_id]
    return {"message": "Garage deleted successfully"}
