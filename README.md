
# Automatización de respuestas de correos de soporte

Proyecto académico desarrollado en Python para clasificar correos de soporte y generar
respuestas formales automáticas.

## Funcionalidades

- Clasificación de correos por categorías.
- Generación automática de respuestas.
- Manejo de excepciones.
- Pruebas unitarias con PyTest.
- Cobertura con pytest-cov.
- Pipeline de Integración Continua con GitHub Actions.

## Estructura

```text
.
├── app.py
├── src/
├── tests/
├── pyproject.toml
├── requirements.txt
└── .github/workflows/python-ci.yml
```

## Ejecución local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Pruebas y cobertura

```bash
python -m flake8 src tests app.py
python -m black --check src tests app.py
python -m pytest
```

El reporte HTML se genera en `htmlcov/index.html`.

## Flujo de ramas

- `main`: versión estable.
- `developer`: integración del trabajo del equipo.
- `staging`: versión validada y lista para despliegue.
