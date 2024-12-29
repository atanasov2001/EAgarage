from fastapi import FastAPI
from routers import garages, cars, maintenance

app = FastAPI()


app.include_router(garages.router, prefix="/garages", tags=["Garages"])
app.include_router(cars.router, prefix="/cars", tags=["Cars"])
app.include_router(maintenance.router, prefix="/maintenance", tags=["Maintenance Requests"])

@app.get("/")
def root():
    return {"message": "2001261059"}
