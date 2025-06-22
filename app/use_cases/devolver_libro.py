from app.domain.entities.libro import Libro
from app.domain.entities.usuario import Usuario


class DevolverLibroUseCase:
    def execute(self, usuario: Usuario, libro: Libro):
        usuario.devolver_libro(libro.id)
        libro.devolver()
        return f"Book '{libro.titulo}' returned by {usuario.nombre}."
