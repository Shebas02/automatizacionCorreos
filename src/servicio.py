from src.clasificador import clasificar_correo
from src.respuestas import generar_respuesta


def procesar_correo(asunto: str, cuerpo: str, nombre: str | None = None) -> dict:
    """Clasifica el correo y devuelve una respuesta automática."""
    categoria = clasificar_correo(asunto, cuerpo)
    respuesta = generar_respuesta(categoria, nombre)
    return {
        "categoria": categoria,
        "respuesta": respuesta,
    }
