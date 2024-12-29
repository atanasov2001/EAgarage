from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int
    garage_id: int


cars = [
    Car(id=1, make="Toyota", model="Corolla", year=2020, garage_id=1),
    Car(id=2, make="Honda", model="Civic", year=2019, garage_id=2),
]

@router.post("/")
def create_car(car: Car):
    cars.append(car)
    return {"message": "Car created successfully", "car": car}


@router.get("/", response_model=List[Car])
def get_all_cars():
    return cars

@router.get("/{car_id}", response_model=Car)
def get_car(car_id: int):
    for car in cars:
        if car.id == car_id:
            return car
    return {"error": "Car not found"}


@router.put("/{car_id}")
def update_car(car_id: int, updated_car: Car):
    for index, car in enumerate(cars):
        if car.id == car_id:
            cars[index] = updated_car
            return {"message": "Car updated successfully", "car": updated_car}
    return {"error": "Car not found"}

@router.delete("/{car_id}")
def delete_car(car_id: int):
    global cars
    cars = [car for car in cars if car.id != car_id]
    return {"message": "Car deleted successfully"}
