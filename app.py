from flask import Flask, request, jsonify, send_from_directory
import spacy
import os

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

responses = {
    "greeting": "Hello! How can I assist you today?",
    "goodbye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! If you have any other questions, feel free to ask."
}

# Serve the HTML file
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Serve static files like CSS
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    doc = nlp(user_input)

    if any([token.lemma_ == "hello" for token in doc]):
        response = responses["greeting"]
    elif any([token.lemma_ == "bye" for token in doc]):
        response = responses["goodbye"]
    elif any([token.lemma_ == "thank" for token in doc]):
        response = responses["thank you"]
    else:
        response = "I'm sorry, I didn't understand that. Could you please rephrase?"

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
