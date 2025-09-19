
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a DentalSoft Backend"}

@app.get("/pacientes")
def get_pacientes():
    return [{"id": 1, "nombre": "Juan Pérez"}, {"id": 2, "nombre": "María Gómez"}]
