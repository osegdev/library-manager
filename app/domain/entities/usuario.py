import uuid
from dataclasses import dataclass, field
from typing import List


@dataclass
class Usuario:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    nombre: str = ""
    correo: str = ""
    libros_prestados: List[str] = field(default_factory=list)

    def prestar_libro(self, libro_id: str):
        if libro_id in self.libros_prestados:
            raise ValueError("This book has already been lent by the user")
        self.libros_prestados.append(libro_id)

    def devolver_libro(self, libro_id: str):
        if libro_id in self.libros_prestados:
            self.libros_prestados.remove(libro_id)
        else:
            raise ValueError("The book is not lent by this user")
