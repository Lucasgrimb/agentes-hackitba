import os
import sys
import json
import base64
from openai import OpenAI

VOICES = {
    "profesional": "onyx",
    "amigable": "nova",
    "narradora": "shimmer",
    "energetico": "echo",
    "neutral": "alloy",
    "dramatico": "fable",
}

def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(json.dumps({"error": "Falta OPENAI_API_KEY en variables de entorno."}))
        sys.exit(1)
        
    input_text = os.environ.get("INPUT_TEXT")
    if not input_text:
        print(json.dumps({"error": "Falta la variable INPUT_TEXT. El usuario debe proveer el script a leer."}))
        sys.exit(1)

    voice_style = os.environ.get("VOICE_STYLE", "profesional").lower()
    voice_id = VOICES.get(voice_style, "onyx")

    quality = os.environ.get("QUALITY", "hd").lower()
    model = "tts-1-hd" if quality == "hd" else "tts-1"
        
    client = OpenAI(api_key=api_key)
    
    try:
        response = client.audio.speech.create(
            model=model,
            voice=voice_id,
            input=input_text
        )
        
        audio_content = response.read()
        b64_audio = base64.b64encode(audio_content).decode('utf-8')
        
        result = {
            "status": "success",
            "agent": "voiceover_pro",
            "voice_style": voice_style,
            "voice_id": voice_id,
            "quality": quality,
            "text_length": len(input_text),
            "audio_base64_mp3": b64_audio
        }
        print(json.dumps(result))
        
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
