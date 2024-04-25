from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Rasa server URL
RASA_SERVER_URL = "http://localhost:5006/model/parse"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']

    # Send the user message to the Rasa server
    response = requests.post(RASA_SERVER_URL, json={"text": user_message})
    rasa_data = response.json()

    # Extract the intent and confidence
    intent = rasa_data['intent']['name']
    confidence = rasa_data['intent']['confidence']

    return jsonify({'intent': intent, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True)





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form.get('user_message')
    # Assuming you have a function to get the Rasa response
    rasa_response = get_rasa_response(user_message)
    
    # Format the response as JSON
    response_data = {
        "confidence": rasa_response["confidence"],
        "intent": rasa_response["intent"]["name"],
        "response": rasa_response["responses"][0]["text"]  # Assuming the response is in the first response
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)