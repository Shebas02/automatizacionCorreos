PLANTILLAS = {
    "acceso": (
        "Estimado usuario:\n\n"
        "Hemos recibido su solicitud relacionada con el acceso al sistema. "
        "El equipo de soporte verificará el estado de sus credenciales y le informará "
        "el resultado de la revisión.\n\nSaludos cordiales."
    ),
    "transferencias": (
        "Estimado usuario:\n\n"
        "Su novedad relacionada con transferencias ha sido registrada. "
        "Se revisarán los datos de la operación y el estado de la transacción.\n\n"
        "Saludos cordiales."
    ),
    "pagos": (
        "Estimado usuario:\n\n"
        "La incidencia asociada al pago fue registrada para validación. "
        "Se verificará el débito, la acreditación y la respuesta del servicio.\n\n"
        "Saludos cordiales."
    ),
    "tarjetas": (
        "Estimado usuario:\n\n"
        "Su solicitud relacionada con tarjetas ha sido recibida. "
        "El caso será revisado conforme a los controles de seguridad establecidos.\n\n"
        "Saludos cordiales."
    ),
    "general": (
        "Estimado usuario:\n\n"
        "Gracias por comunicarse con Mesa de Ayuda. "
        "Su solicitud ha sido registrada y será revisada por el área correspondiente.\n\n"
        "Saludos cordiales."
    ),
}


def generar_respuesta(categoria: str, nombre: str | None = None) -> str:
    """Genera una respuesta formal con base en la categoría detectada."""
    if categoria not in PLANTILLAS:
        raise ValueError(f"Categoría no válida: {categoria}")

    respuesta = PLANTILLAS[categoria]
    if nombre and nombre.strip():
        respuesta = respuesta.replace(
            "Estimado usuario", f"Estimado/a {nombre.strip()}"
        )
    return respuesta
