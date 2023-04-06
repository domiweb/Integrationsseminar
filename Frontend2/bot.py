from flask import Flask, render_template, request, jsonify
import chatbot_model

app = Flask(__name__)
model = chatbot_model.load_model()  # Laden des Chatbot-Modells

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['user_input']  # Abrufen der Nutzereingabe
    response = chatbot_model.predict_class(user_input, model)  # Aufrufen der Funktion mit der Nutzereingabe als Parameter

    return jsonify({'response': response})  # Rückgabe der Antwort des Chatbots als JSON

if __name__ == '__main__':
    app.run(debug=True)
