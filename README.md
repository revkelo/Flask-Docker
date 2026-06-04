# FastAPI + Docker — Render-Ready Starter

Plantilla minimalista para levantar una **API REST con FastAPI** dentro de Docker, lista para desplegar en [Render](https://render.com) con cero configuración extra.

> **Nota:** El nombre del repo refleja el origen del template. La implementación usa **FastAPI** (no Flask).

## Stack

- **FastAPI** 0.115 + **Uvicorn** 0.34
- **Python** 3.12-slim (imagen Docker optimizada)
- **Docker** multi-stage ready
- **Render** deploy via Docker (soporta `$PORT` dinámico)

## Endpoints incluidos

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/` | Hello world |
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Swagger UI (automático) |
| `GET` | `/openapi.json` | Esquema OpenAPI |

## Uso local

```bash
# Con Docker
docker build -t fastapi-api .
docker run --rm -p 8000:8000 fastapi-api

# Sin Docker
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API disponible en `http://localhost:8000` · Docs en `http://localhost:8000/docs`

## Deploy en Render

1. Crear **Web Service** en Render
2. Conectar este repositorio
3. Seleccionar runtime **Docker**
4. Render detecta el `Dockerfile` y gestiona `$PORT` automáticamente

No se necesitan variables de entorno adicionales para el despliegue base.

## Estructura

```
.
├── app/
│   └── main.py        # Aplicación FastAPI
├── Dockerfile         # Imagen Python 3.12-slim + Uvicorn
├── .dockerignore
└── requirements.txt
```

## Extender el template

Agregar un nuevo endpoint en `app/main.py`:

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

Para conectar una base de datos, agregar `sqlalchemy` o `databases` a `requirements.txt` y configurar la conexión como variable de entorno en Render.
