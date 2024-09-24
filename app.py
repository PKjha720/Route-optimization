from flask import Flask, request, jsonify
from src.predictive_model import build_predictive_model  # Import the function to build the model

# Load the model once, at the global level
model = build_predictive_model()
app = Flask(__name__)

# Add this route for the root URL
@app.route('/')
def home():
    return "<h1>Welcome to the Route Optimization API</h1>"

# Your existing predict route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    distance = data['distance']
    traffic = data['traffic']
    volume = data['volume']

    # Assuming you have a model loaded already
    prediction = model.predict([[distance, traffic, volume]])[0]
    return jsonify({'predicted_delivery_time': prediction})

if __name__ == "__main__":
    app.run(debug=True)
