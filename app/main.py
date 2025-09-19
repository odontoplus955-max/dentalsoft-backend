from fastapi import FastAPI

app = FastAPI(title="DentalSoft Backend")

@app.get("/")
def root():
    return {"message": "Bienvenido a DentalSoft Backend"}

@app.get("/pacientes")
def pacientes():
    return [
        {"id": 1, "nombre": "Juan Pérez"},
        {"id": 2, "nombre": "María Gómez"}
    ]
