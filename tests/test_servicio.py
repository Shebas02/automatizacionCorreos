from src.servicio import procesar_correo


def test_procesar_correo():
    resultado = procesar_correo(
        "Error de transferencia",
        "La transferencia no se refleja en la cuenta destino",
        "Carlos",
    )
    assert resultado["categoria"] == "transferencias"
    assert "Carlos" in resultado["respuesta"]
