# app.py
from flask import Flask, request, jsonify
from src.predictive_model import build_predictive_model

app = Flask(__name__)
model = build_predictive_model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    distance = data['distance']
    traffic = data['traffic']
    volume = data['volume']

    prediction = model.predict([[distance, traffic, volume]])[0]
    return jsonify({'predicted_delivery_time': prediction})

if __name__ == "__main__":
    app.run(debug=True)
