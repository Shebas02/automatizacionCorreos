# Automatización de Respuestas de Correos de Soporte

Proyecto desarrollado en **Python** para automatizar la clasificación de correos de soporte y generar respuestas formales de manera automática. El proyecto implementa pruebas unitarias, análisis de calidad de código e integración continua mediante GitHub Actions.

---

## Características

- Clasificación automática de correos por categoría.
- Generación de respuestas automáticas.
- Manejo de excepciones.
- Pruebas unitarias con Pytest.
- Cobertura de código con Pytest-Cov.
- Validación de estilo con Flake8.
- Formateo de código con Black.
- Integración Continua (CI) mediante GitHub Actions.

---

## Estructura del proyecto

```text
.
├── app.py
├── src/
│   ├── clasificador.py
│   ├── respuestas.py
│   ├── servicio.py
│   └── __init__.py
├── tests/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Instalación

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

```bash
python app.py
```

---

## Validación de calidad

Ejecutar Flake8:

```bash
python -m flake8 src tests app.py
```

Verificar formato con Black:

```bash
python -m black --check .
```

---

## Pruebas

Ejecutar todas las pruebas:

```bash
python -m pytest
```

Ejecutar pruebas con cobertura:

```bash
python -m pytest --cov=src --cov-branch --cov-report=term-missing --cov-report=html --cov-fail-under=80
```

El reporte HTML se genera automáticamente en:

```
htmlcov/index.html
```

---

## Integración Continua

El proyecto incorpora un flujo de **GitHub Actions** que ejecuta automáticamente en cada **Push** y **Pull Request**:

- Validación de estilo con Flake8.
- Verificación de formato con Black.
- Ejecución de pruebas unitarias.
- Cálculo de cobertura del código.
- Generación del reporte HTML de cobertura.

---

## Flujo de ramas

- **main** → versión estable.
- **developer** → integración del desarrollo.
- **staging** → versión previa a producción.

---

## Tecnologías utilizadas

- Python 3.11+
- Pytest
- Pytest-Cov
- Flake8
- Black
- Git
- GitHub Actions