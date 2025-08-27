# Smart-Chat-Application
This smart chatbot provides accurate answers, writes code in various programming languages, and assists in building mini applications efficiently.

---
note:
   1   .env file is not here create it and and place GEMINI_API_KEY.
   2   create your own environment and apply this project.


Features:

- Interactive chat interface with user and bot messages.
- Supports Markdown rendering (headings, lists, code blocks, etc.).
- Syntax highlighting for C++, Python, and other programming languages.
- Maintains chat history for the current session.

---

Project Structure:

Smart Chat Application/
│
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend HTML file
├── static/
│   └── style.css        # CSS styling for the app
├── .env                 # Environment file to store your Gemini API key
├── README.md            # Project documentation (this file)


---

Setup Instructions:

1. Clone the repository:

   git clone <your-repo-url>
   cd chatbot_flask

2. Install dependencies:

   pip install flask python-dotenv google-generativeai

3. Configure API Key:

   Create a .env file in the root folder:

   GEMINI_API_KEY=your_gemini_api_key_here 

   Replace your_gemini_api_key_here with your actual Google Gemini API key.

4. Run the app:

   python app.py

   Open your browser and go to:

   http://127.0.0.1:5000/

---

Usage:

1. Type a message or question in the input box.
2. Click Send.
3. Gemini’s response will appear below, formatted with Markdown and highlighted code blocks.

---

Tech Stack:

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- Libraries: Marked.js (Markdown rendering), Highlight.js (code syntax highlighting)
- API: Google Gemini AI

---

Future Improvements:

- Persistent chat history (store in database).
- More polished chat UI with chat bubbles and timestamps.
- Mobile-friendly responsive design.
- Support for attachments or file uploads.
