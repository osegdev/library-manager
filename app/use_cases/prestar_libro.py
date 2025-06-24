from app.domain.entities.historial import HistorialDePrestamo
from app.domain.entities.libro import Libro
from app.domain.entities.usuario import Usuario


class PrestarLibroUseCase:
    def execute(self, usuario, libro):
        if not libro.disponible:
            raise ValueError("El libro no está disponible para préstamo.")

        usuario.prestar_libro(libro.id)
        libro.prestar()

        # 👉 REGISTRO DE HISTORIAL
        historial = HistorialDePrestamo(libro_id=libro.id, usuario_id=usuario.id)
        usuario.registrar_historial(historial)

        return f"Book '{libro.titulo}' lent to {usuario.nombre}."
