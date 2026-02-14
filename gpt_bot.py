from openai import OpenAI
import json

# initialize client
client = OpenAI(api_key="YOUR_API_KEY_HERE")


# load local data so GPT can use project knowledge
def load_data():
    try:
        with open("data/portals.json") as f:
            portals = json.load(f)
    except:
        portals = {}

    try:
        with open("data/helplines.json") as f:
            helplines = json.load(f)
    except:
        helplines = {}

    return portals, helplines


def gpt_chatbot(message, region):

    portals, helplines = load_data()

    system_prompt = f"""
You are a cybersecurity assistant.

Your job:
1. Identify cybercrime type
2. Suggest correct reporting portal
3. Provide step-by-step complaint guidance
4. Suggest helplines if needed

Use this region: {region}

Available portals:
{json.dumps(portals.get(region, []), indent=2)}

Available helplines:
{json.dumps(helplines.get(region, []), indent=2)}

Respond clearly in structured format.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content
