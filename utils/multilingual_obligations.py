import os
from dotenv import load_dotenv
from openai import OpenAI

# Force-load .env outside utils
ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(ENV_PATH)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ----------------------------------------
# Extract Obligations, Rights, Prohibitions
# ----------------------------------------
def extract_obligations_rights(text, lang="en"):

    prompt = f"""
    Extract the following from the contract text below:

    • Obligations (what each party MUST do)
    • Rights (what each party IS ALLOWED to do)
    • Prohibitions (what parties are NOT allowed to do)

    Output MUST be valid JSON with structure:

    {{
        "OBLIGATIONS": [],
        "RIGHTS": [],
        "PROHIBITIONS": []
    }}

    Detect contract structure even if written in {lang}.  
    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[
            {"role": "system", "content": "You are a multilingual contract NLP expert."},
            {"role": "user", "content": prompt}
        ]
    )

    result = response.choices[0].message["content"]

    # Safe JSON parsing
    try:
        import json
        return json.loads(result)
    except:
        return {
            "OBLIGATIONS": [],
            "RIGHTS": [],
            "PROHIBITIONS": [],
            "raw": result
        }
