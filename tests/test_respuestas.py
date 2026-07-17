import pytest
from src.respuestas import generar_respuesta

def test_generar_respuesta_general():
    respuesta = generar_respuesta("general")
    assert "Mesa de Ayuda" in respuesta

def test_generar_respuesta_con_nombre():
    respuesta = generar_respuesta("acceso", "Sebastián")
    assert "Sebastián" in respuesta

def test_categoria_invalida():
    with pytest.raises(ValueError):
        generar_respuesta("desconocida")
