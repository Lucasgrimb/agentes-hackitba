import os
import sys
import json
from openai import OpenAI

STYLES = {
    "minimalista": "minimalist, clean lines, geometric, flat design, modern, single color accent, white background",
    "corporativo": "professional corporate logo, sleek, modern, trustworthy, blue tones, clean typography",
    "startup": "modern tech startup logo, gradient colors, abstract geometric shape, innovative, dynamic",
    "vintage": "vintage retro logo, hand-drawn feel, warm earthy colors, classic typography, badge style",
    "luxury": "luxury premium logo, gold and black, elegant serif typography, sophisticated, high-end brand",
    "playful": "playful colorful logo, friendly, rounded shapes, vibrant palette, fun and approachable",
}

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(json.dumps({"error": "Falta OPENAI_API_KEY en variables de entorno."}))
        sys.exit(1)
        
    brand_description = os.environ.get("PROMPT")
    if not brand_description:
        print(json.dumps({"error": "Falta la variable PROMPT con la descripción de la marca."}))
        sys.exit(1)

    style_name = os.environ.get("STYLE", "startup").lower()
    style_prompt = STYLES.get(style_name, STYLES["startup"])

    variations = min(int(os.environ.get("VARIATIONS", "2")), 3)
        
    client = OpenAI(api_key=api_key)
    
    try:
        logos = []
        
        for i in range(variations):
            variation_hints = [
                "with an abstract icon symbol",
                "with a lettermark monogram using the initials",
                "with a mascot or character element",
            ]
            hint = variation_hints[i % len(variation_hints)]
            
            full_prompt = (
                f"Professional logo design for: {brand_description}. "
                f"Style: {style_prompt}. "
                f"Variation: {hint}. "
                f"The logo must work on both light and dark backgrounds. "
                f"No mockups, no text descriptions, just the isolated logo on a clean white background."
            )
            
            response = client.images.generate(
                model="dall-e-3",
                prompt=full_prompt,
                size="1024x1024",
                quality="hd",
                n=1,
                response_format="url"
            )
            
            logos.append({
                "variation": i + 1,
                "style": style_name,
                "hint": hint,
                "image_url": response.data[0].url
            })
        
        result = {
            "status": "success",
            "agent": "logo_designer_pro",
            "brand": brand_description,
            "style": style_name,
            "total_variations": len(logos),
            "logos": logos
        }
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
