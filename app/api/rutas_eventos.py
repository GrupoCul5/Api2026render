from fastapi import APIRouter, HTTPException
from app.models.evento import Evento
from app.repositories.evento_repo import EventoRepository

router = APIRouter(prefix="/eventos", tags=["Gestión de Eventos"])
repo = EventoRepository()


@router.get("/")
def listar_eventos():
    return repo.obtener_todos()


@router.get("/{evento_id}")
def obtener_evento(evento_id: int):
    evento = repo.obtener_por_id(evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return evento


@router.post("/")
def crear_evento(evento: Evento):
    nuevo_id = repo.crear(evento)
    return {"mensaje": "Evento registrado exitosamente", "id": nuevo_id}


@router.delete("/{evento_id}")
def eliminar_evento(evento_id: int):
    exito = repo.eliminar(evento_id)
    if not exito:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return {"mensaje": "Evento eliminado correctamente"}


@router.put("/{evento_id}")
def actualizar_evento(evento_id: int, evento: Evento):
    exito = repo.actualizar(evento_id, evento)
    if not exito:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return {"mensaje": "Evento actualizado correctamente"}
