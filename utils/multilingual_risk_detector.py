import re

def detect_risks(text, lang="en"):

    risks = []

    patterns = {
        "Termination Clause": r"terminate|termination",
        "Jurisdiction": r"jurisdiction|governed by",
        "Auto-Renewal": r"auto|renew",
        "Penalty Clause": r"penalty|fine",
        "Indemnity": r"indemn",
        "IP Transfer": r"intellectual property|IP"
    }

    for risk, pattern in patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            risks.append(risk)

    risk_level = "Low"
    if len(risks) >= 3:
        risk_level = "Medium"
    if len(risks) >= 5:
        risk_level = "High"

    return {
        "Risk Score": risk_level,
        "Risks Found": risks
    }
