from src.servicio import procesar_correo

def main() -> None:
    print("=== Automatización de respuestas de soporte ===")
    nombre = input("Nombre del usuario (opcional): ")
    asunto = input("Asunto: ")
    cuerpo = input("Mensaje: ")

    try:
        resultado = procesar_correo(asunto, cuerpo, nombre)
        print(f"\nCategoría detectada: {resultado['categoria']}")
        print("\nRespuesta sugerida:\n")
        print(resultado["respuesta"])
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
