from app.domain.entities.libro import Libro
from app.domain.entities.usuario import Usuario


class PrestarLibroUseCase:
    def execute(self, usuario: Usuario, libro: Libro):
        if not libro.disponible:
            raise ValueError("The book is not available to lease")

        usuario.prestar_libro(libro.id)
        libro.prestar()
        return f"Book '{libro.titulo}' lent to {usuario.nombre}."
