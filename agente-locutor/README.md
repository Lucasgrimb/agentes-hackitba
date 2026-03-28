# Agente Locutor Profesional (Voiceover HD)

Convierte texto a voz hiperrealista con 6 estilos de voz y calidad HD.

## Variables de entorno

| Variable | Requerida | Default | Descripción |
|---|---|---|---|
| `OPENAI_API_KEY` | ✅ | — | API Key de OpenAI |
| `INPUT_TEXT` | ✅ | — | Texto a convertir en voz |
| `VOICE_STYLE` | ❌ | `profesional` | Opciones: `profesional`, `amigable`, `narradora`, `energetico`, `neutral`, `dramatico` |
| `QUALITY` | ❌ | `hd` | Opciones: `hd` (alta fidelidad), `standard` (más rápido) |

## Build & Run

```bash
docker build -t agente-locutor .

docker run --rm \
  -e OPENAI_API_KEY="sk-proj-..." \
  -e INPUT_TEXT="Bienvenidos al marketplace de agentes de IA" \
  -e VOICE_STYLE="energetico" \
  agente-locutor
```

## Output (stdout JSON)

```json
{
  "status": "success",
  "agent": "voiceover_pro",
  "voice_style": "energetico",
  "voice_id": "echo",
  "quality": "hd",
  "text_length": 45,
  "audio_base64_mp3": "SUQzBA..."
}
```

El frontend reproduce el audio así:
```html
<audio src="data:audio/mp3;base64,{audio_base64_mp3}" controls></audio>
```
