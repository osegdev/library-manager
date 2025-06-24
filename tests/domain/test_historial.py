from datetime import datetime, timedelta

from app.domain.entities.historial import HistorialDePrestamo


def test_historial_sin_penalizacion():
    h = HistorialDePrestamo(libro_id="1", usuario_id="1")
    h.fecha_prestamo = datetime.now() - timedelta(days=5)
    h.marcar_devolucion()
    assert not h.penalizado


def test_historial_con_penalizacion():
    h = HistorialDePrestamo(libro_id="1", usuario_id="1")
    h.fecha_prestamo = datetime.now() - timedelta(days=10)
    h.marcar_devolucion()
    assert h.penalizado
    assert h.retraso_en_dias() >= 8
