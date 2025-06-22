import pytest

from app.domain.entities.libro import Libro
from app.domain.entities.usuario import Usuario
from app.use_cases.devolver_libro import DevolverLibroUseCase
from app.use_cases.prestar_libro import PrestarLibroUseCase


@pytest.fixture
def libro_disponible():
    return Libro(
        titulo="100 years of solitude", autor="G. G. Márquez", anio_publicacion=1967
    )


@pytest.fixture
def usuario():
    return Usuario(nombre="Carlos Reyes", correo="carlos@example.com")


def test_prestar_libro_exitoso(libro_disponible, usuario):
    use_case = PrestarLibroUseCase()
    mensaje = use_case.execute(usuario, libro_disponible)
    assert not libro_disponible.disponible
    assert libro_disponible.id in usuario.libros_prestados
    assert "lent" in mensaje


def test_prestar_libro_no_disponible(libro_disponible, usuario):
    libro_disponible.disponible = False
    use_case = PrestarLibroUseCase()
    with pytest.raises(ValueError, match="not available to lease"):
        use_case.execute(usuario, libro_disponible)


def test_devolver_libro_exitoso(libro_disponible, usuario):
    use_case_prestar = PrestarLibroUseCase()
    use_case_prestar.execute(usuario, libro_disponible)

    use_case_devolver = DevolverLibroUseCase()
    mensaje = use_case_devolver.execute(usuario, libro_disponible)
    assert libro_disponible.disponible
    assert libro_disponible.id not in usuario.libros_prestados
    assert "returned" in mensaje


def test_devolver_libro_no_prestado(libro_disponible, usuario):
    use_case_devolver = DevolverLibroUseCase()
    with pytest.raises(ValueError, match="not lent by this user"):
        use_case_devolver.execute(usuario, libro_disponible)
