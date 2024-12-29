from pydantic import BaseModel

class MaintenanceRequest(BaseModel):
    id: int
    car_id: int
    service_type: str
    scheduled_date: str
    garage_id: int
