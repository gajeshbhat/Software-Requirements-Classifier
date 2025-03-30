import requests
import json
import re

def classify_requirements_via_api(requirements, model="codellama:instruct"):
    prompt = f"""
You are a JSON API. Classify the following software requirements into one of:
- Functional
- Non-Functional
- Ambiguous
- Incomplete

Return ONLY a JSON array in this format:
[
  {{ "requirement": "...", "label": "..." }},
  ...
]

Do NOT include any prose, explanations, or markdown — only valid JSON.
Here are the requirements:
{requirements}
"""

    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        })

        content = response.json().get('response', '')

        # Extract JSON array
        json_blob_match = re.search(r'\[\s*{.*?}\s*\]', content, re.DOTALL)
        if not json_blob_match:
            raise ValueError("No JSON array found in response.")

        raw_json = json_blob_match.group(0)

        # Clean common LLM junk
        raw_json = raw_json.replace("...", "")
        raw_json = re.sub(r'{\s*}', '', raw_json)
        raw_json = re.sub(r',\s*\]', ']', raw_json)
        raw_json = re.sub(r'\[[^\]]*\]\([^)]+\)', '', raw_json)  # Remove markdown links [text](url)
        raw_json = re.sub(r'\[.*?\]', '', raw_json)  # Remove remaining [brackets]

        parsed = json.loads(raw_json)
        return parsed

    except Exception as e:
        print(f"⚠️ API failed to parse response: {e}")
        with open("llm_output_debug.txt", "w") as f:
            f.write(content)

    # fallback
    print("⚠️ Falling back to Unclassified for each requirement.")
    return [{"requirement": line.strip(), "label": "Unclassified"}
            for line in requirements.splitlines()
            if line.strip() and not line.strip().startswith("#")]
