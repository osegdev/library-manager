from app.domain.entities.libro import Libro
from app.domain.entities.usuario import Usuario
from app.use_cases.devolver_libro import DevolverLibroUseCase
from app.use_cases.prestar_libro import PrestarLibroUseCase

libro = Libro(titulo="1984", autor="George Orwell", anio_publicacion=1949)
usuario = Usuario(nombre="Ana Pérez", correo="ana@example.com")
prestar = PrestarLibroUseCase()
devolver = DevolverLibroUseCase()

print(libro)
print(usuario)
print(prestar.execute(usuario, libro))  # Debería prestar el libro
print(devolver.execute(usuario, libro))  # Debería devolver el libro
