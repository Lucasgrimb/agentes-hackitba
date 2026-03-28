# Agente Diseñador de Logos Pro

Genera múltiples variaciones de logos profesionales con estilos predefinidos y calidad HD usando DALL-E 3.

## Variables de entorno

| Variable | Requerida | Default | Descripción |
|---|---|---|---|
| `OPENAI_API_KEY` | ✅ | — | API Key de OpenAI |
| `PROMPT` | ✅ | — | Descripción de la marca/empresa |
| `STYLE` | ❌ | `startup` | Opciones: `minimalista`, `corporativo`, `startup`, `vintage`, `luxury`, `playful` |
| `VARIATIONS` | ❌ | `2` | Cantidad de variaciones a generar (1 a 3) |

## Build & Run

```bash
docker build -t agente-logo .

docker run --rm \
  -e OPENAI_API_KEY="sk-proj-..." \
  -e PROMPT="Cafetería artesanal llamada El Grano de Oro" \
  -e STYLE="vintage" \
  -e VARIATIONS="3" \
  agente-logo
```

## Output (stdout JSON)

```json
{
  "status": "success",
  "agent": "logo_designer_pro",
  "brand": "Cafetería artesanal...",
  "style": "vintage",
  "total_variations": 3,
  "logos": [
    { "variation": 1, "style": "vintage", "hint": "with an abstract icon symbol", "image_url": "https://..." },
    { "variation": 2, "style": "vintage", "hint": "with a lettermark monogram", "image_url": "https://..." },
    { "variation": 3, "style": "vintage", "hint": "with a mascot element", "image_url": "https://..." }
  ]
}
```

El frontend muestra cada `image_url` como imagen. Los links expiran en 24hs.
