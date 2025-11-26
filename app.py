from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')
CORS(app)  # To avoid CORS issues if testing from separate server

# Load models
soil_model = pickle.load(open("model\\soil_model.pkl", "rb"))
crop_model = pickle.load(open("model\\crop_model.pkl", "rb"))

# Optional: Load encoders if used
soil_encoder = pickle.load(open("model\\soil_encoder.pkl", "rb"))
crop_encoder = pickle.load(open("model\\crop_encoder.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_all", methods=["POST"])
@app.route("/predict_all", methods=["POST"])
def predict_all():
    try:
        data = request.get_json()

        pH = float(data["pH"])
        rainfall = float(data["rainfall"])
        humidity = float(data["humidity"])
        temperature = float(data["temperature"])
        N = float(data["N"])
        P = float(data["P"])
        K = float(data["K"])

        # Soil prediction
        soil_input = np.array([[N, P, K, temperature, humidity, pH, rainfall]])
        soil_pred = soil_model.predict(soil_input)
        soil_label = soil_encoder.inverse_transform(soil_pred)[0]
        soil_label = str(soil_label)

        # Crop prediction
        crop_input = np.array([[N, P, K, temperature, humidity, pH, rainfall]])
        crop_pred = crop_model.predict(crop_input)
        crop_label = crop_encoder.inverse_transform(crop_pred)[0]
        crop_label = str(crop_label)

        return jsonify({
            "soil_type": soil_label,
            "crop_type": crop_label
        })

    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == "__main__":
    app.run(debug=True)
