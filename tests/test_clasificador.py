import pytest
from src.clasificador import clasificar_correo

@pytest.mark.parametrize(
    "asunto,cuerpo,esperado",
    [
        ("Problema de acceso", "No puedo ingresar con mi contraseña", "acceso"),
        ("Transferencia", "La transferencia no llegó a la cuenta destino", "transferencias"),
        ("Pago duplicado", "Se realizó un débito por un pago", "pagos"),
        ("Bloqueo de tarjeta", "Necesito bloquear mi tarjeta Visa", "tarjetas"),
        ("Consulta", "Necesito información adicional", "general"),
    ],
)
def test_clasificar_correo(asunto, cuerpo, esperado):
    assert clasificar_correo(asunto, cuerpo) == esperado

def test_correo_vacio():
    with pytest.raises(ValueError):
        clasificar_correo("", "")

def test_tipo_incorrecto():
    with pytest.raises(TypeError):
        clasificar_correo(None, "mensaje")
