PALABRAS_CLAVE = {
    "acceso": ["ingresar", "login", "contraseña", "clave", "acceso", "bloqueado"],
    "transferencias": [
        "transferencia",
        "envío de dinero",
        "beneficiario",
        "cuenta destino",
    ],
    "pagos": ["pago", "débito", "factura", "recaudación", "cobro"],
    "tarjetas": ["tarjeta", "pin", "bloqueo", "visa"],
}


def clasificar_correo(asunto: str, cuerpo: str) -> str:
    """Clasifica un correo de soporte según palabras clave."""
    if not isinstance(asunto, str) or not isinstance(cuerpo, str):
        raise TypeError("El asunto y el cuerpo deben ser texto.")

    contenido = f"{asunto} {cuerpo}".lower().strip()
    if not contenido:
        raise ValueError("El correo no puede estar vacío.")

    puntuaciones = {
        categoria: sum(1 for palabra in palabras if palabra in contenido)
        for categoria, palabras in PALABRAS_CLAVE.items()
    }

    categoria, puntaje = max(puntuaciones.items(), key=lambda item: item[1])
    return categoria if puntaje > 0 else "general"
