from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class HistorialDePrestamo:
    libro_id: str
    usuario_id: str
    fecha_prestamo: datetime = field(default_factory=datetime.now)
    fecha_devolucion: Optional[datetime] = None
    penalizado: bool = False

    def marcar_devolucion(self):
        self.fecha_devolucion = datetime.now()
        if self.retraso_en_dias() > 7:
            self.penalizado = True

    def retraso_en_dias(self) -> int:
        fecha_fin = self.fecha_devolucion or datetime.now()
        return (fecha_fin - self.fecha_prestamo).days
