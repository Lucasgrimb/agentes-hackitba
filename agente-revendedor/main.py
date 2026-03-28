import os
import sys
import json
from openai import OpenAI

PLATFORMS = {
    "mercadolibre": {
        "name": "MercadoLibre",
        "currency": "ARS",
        "tips": "Usar palabras clave que la gente busca en ML. Título máximo 60 caracteres. Incluir marca, modelo y estado."
    },
    "marketplace": {
        "name": "Facebook Marketplace",
        "currency": "ARS",
        "tips": "Título corto y directo. Descripción informal pero completa. Mencionar zona de entrega."
    },
    "amazon": {
        "name": "Amazon",
        "currency": "USD",
        "tips": "Bullet points con beneficios. Título con marca + modelo + característica clave. Descripción tipo ficha técnica."
    },
}

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(json.dumps({"error": "Falta OPENAI_API_KEY en variables de entorno."}))
        sys.exit(1)

    image_url = os.environ.get("IMAGE_URL")
    if not image_url:
        print(json.dumps({"error": "Falta la variable IMAGE_URL con el link a la foto del producto."}))
        sys.exit(1)

    platform = os.environ.get("PLATFORM", "mercadolibre").lower()
    platform_info = PLATFORMS.get(platform, PLATFORMS["mercadolibre"])

    condition = os.environ.get("CONDITION", "usado")

    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"""Sos un experto en ventas online con 10 años de experiencia en {platform_info['name']}.
Tu trabajo es analizar la foto de un producto y generar una publicación profesional lista para copiar y pegar.

REGLAS:
- Identificá el producto exacto: marca, modelo, estado visible, accesorios incluidos.
- Si ves detalles de desgaste (rayones, suciedad, cables pelados), mencionalo honestamente pero con giro positivo.
- El título debe ser SEO-optimizado para la plataforma ({platform_info['tips']}).
- La descripción debe generar urgencia y confianza.
- Estimá un rango de precio realista en {platform_info['currency']} basado en el mercado actual para ese producto en estado {condition}.
- Sugerí 5 tags/palabras clave que un comprador buscaría.

IMPORTANTE: Respondé EXCLUSIVAMENTE con un JSON válido (sin bloques de código markdown). El JSON debe tener esta estructura exacta:
{{
    "producto_detectado": "Qué es exactamente lo que ves en la foto",
    "titulo_publicacion": "Título SEO optimizado listo para pegar",
    "descripcion": "Descripción persuasiva completa con emojis y formato",
    "precio_sugerido_min": numero,
    "precio_sugerido_max": numero,
    "moneda": "{platform_info['currency']}",
    "estado_detectado": "Lo que se ve del estado físico del producto",
    "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"],
    "consejos_para_vender": "Tip específico para mejorar la venta de este producto"
}}"""
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Analizá esta foto de un producto que quiero vender como '{condition}' en {platform_info['name']}. Generame la publicación completa."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": image_url,
                                "detail": "high"
                            }
                        }
                    ]
                }
            ],
            max_tokens=1500,
            temperature=0.7,
        )

        raw_text = response.choices[0].message.content.strip()
        
        # Limpiar si viene envuelto en ```json ... ```
        if raw_text.startswith("```"):
            raw_text = raw_text.split("\n", 1)[1]  # quitar primera línea ```json
            raw_text = raw_text.rsplit("```", 1)[0]  # quitar último ```
            raw_text = raw_text.strip()

        listing_data = json.loads(raw_text)

        result = {
            "status": "success",
            "agent": "revendedor_experto",
            "platform": platform_info["name"],
            "condition": condition,
            "listing": listing_data
        }
        print(json.dumps(result, ensure_ascii=False))

    except json.JSONDecodeError:
        # Si el LLM no devolvió JSON limpio, mandamos el texto crudo
        result = {
            "status": "success",
            "agent": "revendedor_experto",
            "platform": platform_info["name"],
            "condition": condition,
            "listing_raw": raw_text
        }
        print(json.dumps(result, ensure_ascii=False))

    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
