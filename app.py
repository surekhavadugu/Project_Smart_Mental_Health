from flask import Flask, render_template, request, jsonify
from utils.gemini_api import get_gemini_answer
from face_emotion import detect_emotion
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_input = request.form["question"]
        if not user_input.strip():
            return jsonify({"answer": "Please enter a valid message."})

        response = get_gemini_answer(user_input)
        print("Gemini Response:", response) 

        if not response or response.startswith("Error:"):
            return jsonify({"answer": "Sorry, I encountered an issue while processing your request."})

        return jsonify({"answer": response})

    except Exception as e:
        print(f" Flask error in /ask: {e}")
        return jsonify({"answer": "Sorry, something went wrong on the server."})

@app.route("/detect_emotion", methods=["GET"])
def detect_emotion_route():
    try:
        print("Starting emotion detection...")
        quote = detect_emotion()
        print("Emotion detection complete.")
        return jsonify({"quote": quote})
    except Exception as e:
        print(f" Flask error in /detect_emotion: {e}")
        return jsonify({"error": "Could not detect emotion. Please try again."})

if __name__ == "__main__":
    print("Smart Mental Health Companion running at: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
