from fastapi import FastAPI
from garages import router as garage_router

app = FastAPI()

app.include_router(garage_router, prefix="/garages")

@app.get("/")
def read_root():
    return {"message": "2001261059"}
