from langdetect import detect
import re

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def extract_entities(text, lang="en"):

    parties = []
    amounts = []
    dates = []
    jurisdiction = []

    amount_pattern = r"(₹\s?\d+[,0-9]*)"
    date_pattern = r"(\d{1,2}\s?\w+\s?\d{4})"
    city_pattern = r"(Chennai|Delhi|Mumbai|Bangalore|Hyderabad|India|Tamil Nadu|Karnataka)"

    for line in text.split("\n"):
        if " Pvt" in line or " Ltd" in line or "Company" in line:
            parties.append(line.strip())

    amounts.extend(re.findall(amount_pattern, text))
    dates.extend(re.findall(date_pattern, text))
    jurisdiction.extend(re.findall(city_pattern, text))

    return {
        "language": lang,
        "entities": {
            "PARTIES": parties,
            "AMOUNTS": amounts,
            "DATES": dates,
            "JURISDICTION": jurisdiction
        }
    }

