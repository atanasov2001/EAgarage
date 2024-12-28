from pydantic import BaseModel

class Car(BaseModel):
    id: int
    make: str
    model: str
    year: int
    garage_id: int
