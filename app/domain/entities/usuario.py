import uuid
from dataclasses import dataclass, field
from typing import List

from app.domain.entities.historial import HistorialDePrestamo


@dataclass
class Usuario:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    nombre: str = ""
    correo: str = ""
    libros_prestados: List[str] = field(default_factory=list)
    historial: List[HistorialDePrestamo] = field(default_factory=list)
    penalizado: bool = False

    def prestar_libro(self, libro_id: str):
        if libro_id in self.libros_prestados:
            raise ValueError("This book has already been lent by the user")
        self.libros_prestados.append(libro_id)

    def devolver_libro(self, libro_id: str):
        if libro_id in self.libros_prestados:
            self.libros_prestados.remove(libro_id)
        else:
            raise ValueError("The book is not lent by this user")

    def registrar_historial(self, historial: HistorialDePrestamo):
        self.historial.append(historial)

    def aplicar_penalizacion(self):
        self.penalizado = True

    def limpiar_penalizacion(self):
        self.penalizado = False
