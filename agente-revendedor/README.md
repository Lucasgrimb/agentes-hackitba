# Agente Revendedor Experto

Analiza una foto de cualquier producto usando **GPT-4o Vision** y genera una publicación profesional de e-commerce lista para copiar y pegar en MercadoLibre, Facebook Marketplace o Amazon.

## Variables de entorno

| Variable | Requerida | Default | Descripción |
|---|---|---|---|
| `OPENAI_API_KEY` | ✅ | — | API Key de OpenAI |
| `IMAGE_URL` | ✅ | — | URL pública de la foto del producto |
| `PLATFORM` | ❌ | `mercadolibre` | Opciones: `mercadolibre`, `marketplace`, `amazon` |
| `CONDITION` | ❌ | `usado` | Estado del producto: `nuevo`, `usado`, `reacondicionado` |

## Build & Run

```bash
docker build -t agente-revendedor .

docker run --rm \
  -e OPENAI_API_KEY="sk-proj-..." \
  -e IMAGE_URL="https://ejemplo.com/foto-producto.jpg" \
  -e PLATFORM="mercadolibre" \
  -e CONDITION="usado" \
  agente-revendedor
```

## Output (stdout JSON)

```json
{
  "status": "success",
  "agent": "revendedor_experto",
  "platform": "MercadoLibre",
  "condition": "usado",
  "listing": {
    "producto_detectado": "PlayStation 4 Slim 1TB con joystick DualShock 4",
    "titulo_publicacion": "PlayStation 4 Slim 1TB + Joystick Original - Excelente Estado",
    "descripcion": "🎮 PlayStation 4 Slim 1TB en perfecto funcionamiento...",
    "precio_sugerido_min": 180000,
    "precio_sugerido_max": 250000,
    "moneda": "ARS",
    "estado_detectado": "Mínimos signos de uso, sin rayones profundos",
    "tags": ["ps4", "playstation 4", "consola usada", "gaming", "joystick"],
    "consejos_para_vender": "Sacá una foto con los cables ordenados y el joystick apoyado encima"
  }
}
```

## Prueba local (sin Docker)

```bash
OPENAI_API_KEY="tu-key" IMAGE_URL="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/PS4-Console-wDS4.jpg/1200px-PS4-Console-wDS4.jpg" python3 main.py
```
