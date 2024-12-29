from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class MaintenanceRequest(BaseModel):
    id: int
    car_id: int
    service_type: str
    scheduled_date: str
    garage_id: int

maintenance_requests = [
    MaintenanceRequest(id=1, car_id=1, service_type="Oil Change", scheduled_date="2024-01-15", garage_id=1),
    MaintenanceRequest(id=2, car_id=2, service_type="Brake Inspection", scheduled_date="2024-01-20", garage_id=2),
]


@router.post("/")
def create_request(request: MaintenanceRequest):
    maintenance_requests.append(request)
    return {"message": "Maintenance request created successfully", "request": request}


@router.get("/", response_model=List[MaintenanceRequest])
def get_all_requests():
    return maintenance_requests


@router.get("/{request_id}", response_model=MaintenanceRequest)
def get_request(request_id: int):
    for request in maintenance_requests:
        if request.id == request_id:
            return request
    return {"error": "Request not found"}


@router.put("/{request_id}")
def update_request(request_id: int, updated_request: MaintenanceRequest):
    for index, request in enumerate(maintenance_requests):
        if request.id == request_id:
            maintenance_requests[index] = updated_request
            return {"message": "Request updated successfully", "request": updated_request}
    return {"error": "Request not found"}


@router.delete("/{request_id}")
def delete_request(request_id: int):
    global maintenance_requests
    maintenance_requests = [request for request in maintenance_requests if request.id != request_id]
    return {"message": "Request deleted successfully"}
