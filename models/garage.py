from pydantic import BaseModel

class Garage(BaseModel):
    id: int
    name: str
    address: str
