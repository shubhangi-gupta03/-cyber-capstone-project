import requests
from bs4 import BeautifulSoup
import json

def fetch_advisories():

    url = "https://example.com/cyber-alerts"   # replace later with real source
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "html.parser")

    advisories = []

    for item in soup.find_all("h2"):
        advisories.append({
            "title": item.text,
            "type": "Advisory",
            "time": "Latest"
        })

    # save to JSON
    with open("data/advisories.json", "w") as f:
        json.dump({"US": advisories, "FI": advisories}, f, indent=4)

    print("Advisories updated!")
