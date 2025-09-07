
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import getpass
from langchain.chat_models import init_chat_model

# Load API key
load_dotenv()
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

# Initialize the model with LangChain
model = init_chat_model(
    "gemini-2.5-flash",
    model_provider="google_genai",
    temperature=0.2
)

# Flask app
app = Flask(__name__)

# Chat history
chat_history = []

def QandA(query):
    response = model.invoke(query)
    return response.content or "Sorry, I could not generate a response."

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
