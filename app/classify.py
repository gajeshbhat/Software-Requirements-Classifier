from app.ollama_client import classify_requirements_via_api

def classify_text(text: str):
    return classify_requirements_via_api(text)