from datetime import datetime
from app.core.database import Database
from app.models.evento import Evento


class EventoRepository:
    def __init__(self):
        # Composición: el repositorio instancia su propia conexión
        self.db = Database()

    def obtener_todos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM eventos ORDER BY id DESC;")
        eventos = cursor.fetchall()
        conn.close()
        return eventos

    def obtener_por_id(self, evento_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM eventos WHERE id = %s;", (evento_id,))
        evento = cursor.fetchone()
        conn.close()
        return evento

    def crear(self, evento: Evento):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        ahora = datetime.now()
        fecha = evento.fecha or ahora.date()
        hora = evento.hora or ahora.time()

        query = """
            INSERT INTO eventos (fecha, hora, evento, estado, descripcion)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        cursor.execute(query, (fecha, hora, evento.evento, evento.estado, evento.descripcion))
        nuevo_id = cursor.fetchone()["id"]
        conn.commit()
        conn.close()
        return nuevo_id

    def eliminar(self, evento_id: int):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM eventos WHERE id = %s RETURNING id;", (evento_id,))
        eliminado = cursor.fetchone()
        conn.commit()
        conn.close()
        return eliminado is not None

    def actualizar(self, evento_id: int, evento: Evento):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE eventos
            SET evento = %s, estado = %s, descripcion = %s
            WHERE id = %s
            RETURNING id;
        """
        cursor.execute(query, (evento.evento, evento.estado, evento.descripcion, evento_id))
        actualizado = cursor.fetchone()
        conn.commit()
        conn.close()
        return actualizado is not None
