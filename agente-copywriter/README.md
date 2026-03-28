# Agente Copywriter SEO Pro

Genera artículos de blog profesionales optimizados para SEO con meta tags, keywords y call to action.

## Variables de entorno

| Variable | Requerida | Default | Descripción |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | ✅ | — | API Key de Anthropic |
| `TOPIC` | ✅ | — | Tema del artículo |
| `TONE` | ❌ | `profesional` | Opciones: `profesional`, `casual`, `técnico`, `persuasivo` |
| `LANGUAGE` | ❌ | `español` | Opciones: `español`, `inglés` |

## Build & Run

```bash
docker build -t agente-copywriter .

docker run --rm \
  -e ANTHROPIC_API_KEY="sk-ant..." \
  -e TOPIC="Inteligencia artificial en la educación" \
  -e TONE="persuasivo" \
  agente-copywriter
```

## Output (stdout JSON)

```json
{
  "status": "success",
  "agent": "copywriter_seo_pro",
  "topic": "...",
  "tone": "persuasivo",
  "language": "español",
  "result_markdown": "# Título del artículo\n\n..."
}
```

El campo `result_markdown` contiene el artículo completo en Markdown + Meta Title + Meta Description + 5 Keywords SEO al final.
