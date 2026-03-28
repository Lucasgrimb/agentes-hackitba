import os
import sys
import json
import anthropic

def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print(json.dumps({"error": "Falta ANTHROPIC_API_KEY en variables de entorno."}))
        sys.exit(1)
        
    topic = os.environ.get("TOPIC")
    if not topic:
        print(json.dumps({"error": "Falta la variable TOPIC. El usuario debe ingresar sobre qué escribir."}))
        sys.exit(1)

    tone = os.environ.get("TONE", "profesional")
    language = os.environ.get("LANGUAGE", "español")
        
    client = anthropic.Anthropic(api_key=api_key)
    
    prompt = f"""Sos un redactor SEO de élite con 15 años de experiencia escribiendo contenido viral para blogs corporativos.
Tu trabajo es crear un artículo que posicione en la primera página de Google.

TEMA: '{topic}'
TONO: {tone}
IDIOMA: {language}

INSTRUCCIONES ESTRICTAS:
1. Escribí un título H1 irresistible que genere curiosidad y contenga la keyword principal.
2. Abrí con un párrafo "gancho" de 2 oraciones que enganche al lector y lo obligue a seguir leyendo.
3. Usá subtítulos H2 y H3 que sean descriptivos y contengan variaciones de la keyword.
4. Incluí viñetas y listas numeradas para mejorar la legibilidad.
5. Agregá datos concretos, estadísticas o ejemplos reales cuando sea posible.
6. Cerrá con una conclusión que incluya un "call to action" claro.
7. El artículo debe tener entre 800 y 1200 palabras.
8. Incluí al final una sección "---" separada con:
   - Meta Title (máx 60 caracteres)
   - Meta Description (máx 155 caracteres) 
   - 5 Keywords sugeridas para SEO

FORMATO: Devolvé SOLO el contenido en Markdown limpio sin comentarios meta tuyos."""
    
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=4000,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )
        article_content = response.content[0].text
        
        result = {
            "status": "success",
            "agent": "copywriter_seo_pro",
            "topic": topic,
            "tone": tone,
            "language": language,
            "result_markdown": article_content
        }
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
