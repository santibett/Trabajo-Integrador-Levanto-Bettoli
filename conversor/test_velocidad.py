from validaciones import velocidad
import pytest

def test_error_de_tipo():
    with pytest.raises(ValueError):
        velocidad("hola")

def test_menor():
    assert velocidad(-1)==True

def test_mayor():
    assert velocidad(8)==False