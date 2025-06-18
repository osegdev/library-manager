from app.domain.entities.libro import Libro
from app.domain.entities.usuario import Usuario

libro = Libro(titulo="1984", autor="George Orwell", anio_publicacion=1949)
usuario = Usuario(nombre="Ana Pérez", correo="ana@example.com")

print(libro)
print(usuario)
