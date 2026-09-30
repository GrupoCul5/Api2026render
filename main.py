from fastapi import FastAPI
from app.api import rutas_eventos

app = FastAPI(
    title="API de Monitoreo de Sensores",
    description="Backend modular para el sistema de monitoreo (ESP32 + SRF05 + IR) usando FastAPI y PostgreSQL puro",
    version="1.0.0"
)

# Conectamos el módulo de rutas a la aplicación principal
app.include_router(rutas_eventos.router)


@app.get("/")
def estado_api():
    return {"mensaje": "La API de monitoreo se encuentra en línea y funcional"}
