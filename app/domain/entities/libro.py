import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Libro:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    titulo: str = ""
    autor: str = ""
    anio_publicacion: int = 0
    disponible: bool = True
    fecha_registro: datetime = field(default_factory=datetime.now)

    def prestar(self):
        if not self.disponible:
            raise ValueError("The book has already been lent")
        self.disponible = False

    def devolver(self):
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} by {self.autor} ({self.anio_publicacion})"
