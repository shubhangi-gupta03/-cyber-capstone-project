import json

def load_portals():
    with open("data/portals.json") as f:
        return json.load(f)

portals = load_portals()

def detect_crime(message):

    message = message.lower()

    if "fraud" in message:
        return "Financial Fraud"

    if "identity" in message:
        return "Identity Theft"

    if "phishing" in message:
        return "Phishing"

    if "scam" in message:
        return "Online Scam"

    return None


def chatbot_response(message, region):

    crime = detect_crime(message)

    if not crime:
        return "Please describe the cybercrime (fraud, scam, phishing, identity theft)."

    for p in portals.get(region, []):
        if p["crime"].lower() == crime.lower():
            steps = "\n".join(p["steps"])
            return f"""
Cybercrime Detected: {crime}

Recommended Portal: {p['portal']}

Steps to File Complaint:
{steps}
"""

    return "No portal found for this crime."
