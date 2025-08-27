import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash")

# Flask app
app = Flask(__name__)

# Chat history
chat_history = []

def QandA(query):
    response = model.generate_content(query)
    return response.text or "Sorry, I could not generate a response."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("query")
    response_text = QandA(user_input)
    
    # Store in history
    chat_history.append({"user": user_input, "bot": response_text})
    
    return jsonify({"response": response_text, "history": chat_history})

if __name__ == "__main__":
    app.run(debug=True)
