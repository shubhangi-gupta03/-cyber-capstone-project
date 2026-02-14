import requests
import json

def fetch_news():

    API_KEY = "YOUR_API_KEY"

    url = f"https://newsapi.org/v2/everything?q=cybercrime&apiKey={API_KEY}"
    r = requests.get(url)
    data = r.json()

    news_list = []

    for article in data.get("articles", [])[:5]:
        news_list.append({
            "title": article["title"],
            "type": "News",
            "time": "Latest"
        })

    with open("data/advisories.json", "w") as f:
        json.dump({"US": news_list, "FI": news_list}, f, indent=4)

    print("News updated!")
