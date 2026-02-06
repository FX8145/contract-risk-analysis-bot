import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_language(text: str) -> str:
    prompt = f"Detect the language of the following text and ONLY return the language name:\n{text}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    lang = response.choices[0].message.content.strip()
    return lang.lower()

def multilingual_ner(text: str, lang: str):
    prompt = f"""
Extract PARTIES, AMOUNTS, DATES, JURISDICTION from the following {lang} contract text.
Return the answer as normal text paragraphs, not JSON, not code blocks.

Text:
{text}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def extract_obligations_rights(text: str, lang: str):
    prompt = f"""
From the following {lang} contract text, extract:

• Obligations  
• Rights  
• Prohibitions  

Write output in clear paragraphs — NOT as code blocks and NOT as lists.

Text:
{text}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def detect_risks(text: str, lang: str):
    prompt = f"""
Analyze the following {lang} contract text and identify risks:

• Termination  
• Jurisdiction  
• Auto-Renewal  
• Penalty  
• Indemnity  
• IP Transfer  

Write result as clean paragraphs. Do not output JSON.

Text:
{text}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

