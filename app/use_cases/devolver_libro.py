from app.domain.entities.libro import Libro
from app.domain.entities.usuario import Usuario


class DevolverLibroUseCase:
    def execute(self, usuario: Usuario, libro: Libro):
        usuario.devolver_libro(libro.id)
        libro.devolver()

        for registro in usuario.historial:
            if registro.libro_id == libro.id and registro.fecha_devolucion is None:
                registro.marcar_devolucion()
                if registro.penalizado:
                    usuario.aplicar_penalizacion()
                break

        return f"Book '{libro.titulo}' returned by {usuario.nombre}."
