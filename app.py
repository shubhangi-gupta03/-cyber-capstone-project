from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# ===============================
# FLASK APP INIT
# ===============================
app = Flask(__name__)

# ===============================
# GEMINI API CONFIG
# ===============================
# 🔐 Put your NEW Gemini API key here
genai.configure(api_key="AIzaSyCpew110hamjlN4nr7Dm6YSLlRd52wYPpw")

# ✅ Working free model
model = genai.GenerativeModel("gemini-1.5-flash")


# ===============================
# COMPLAINT STEP GENERATOR
# ===============================
def get_complaint_steps(crime_type):

    data = {
        "Online Scam": {
            "portal": "National Cyber Crime Reporting Portal",
            "helpline": "1930",
            "steps": [
                "Collect screenshots and transaction proof",
                "Block bank account/card immediately",
                "Report on cybercrime portal",
                "Call helpline 1930",
                "Follow police instructions"
            ]
        },

        "UPI Fraud": {
            "portal": "Cyber Financial Fraud Portal",
            "helpline": "1930",
            "steps": [
                "Contact bank immediately",
                "Freeze UPI ID",
                "Save transaction details",
                "File complaint online",
                "Monitor bank account"
            ]
        },

        "Cyberbullying": {
            "portal": "Police Cyber Cell",
            "helpline": "112",
            "steps": [
                "Take screenshots",
                "Block offender",
                "Report platform",
                "File police complaint",
                "Seek legal support"
            ]
        }
    }

    return data.get(crime_type, {
        "portal": "Cyber Crime Reporting Portal",
        "helpline": "1930",
        "steps": [
            "Collect evidence",
            "Report cyber portal",
            "Contact police"
        ]
    })


# ===============================
# ROUTES
# ===============================

# Home Dashboard
@app.route("/")
def home():
    return render_template("dashboard.html")


# Complaint Steps API
@app.route("/get_steps", methods=["POST"])
def steps():
    crime_type = request.json["crime"]
    result = get_complaint_steps(crime_type)
    return jsonify(result)


# ===============================
# AI CHATBOT ROUTE
# ===============================
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    user_message = data.get("message", "")
    region = data.get("region", "")

    prompt = f"""
You are an AI Cyber Crime Complaint Assistant.

User region: {region}
User problem: {user_message}

Provide:
- Steps to file complaint
- Official reporting portal for that region
- Helpline number
- Safety advice
- Prevention tips
"""

    try:
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({
            "reply": "Error connecting to AI. Check API key or internet.",
            "error": str(e)
        })


# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
