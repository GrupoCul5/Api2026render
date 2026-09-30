from pydantic import BaseModel
from typing import Optional
from datetime import date, time


class Evento(BaseModel):
    id: Optional[int] = None
    fecha: Optional[date] = None   # si no se envía, el repositorio pone la fecha actual
    hora: Optional[time] = None    # si no se envía, el repositorio pone la hora actual
    evento: str
    estado: str
    descripcion: Optional[str] = ""
