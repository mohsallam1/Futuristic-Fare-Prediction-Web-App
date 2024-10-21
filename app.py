from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Load the model, scaler, and encoders
model = joblib.load(r'C:\Users\mohsa\Downloads\ai\advanced surveillance\intern\weak7\model.pkl')
scaler = joblib.load(r'C:\Users\mohsa\Downloads\ai\advanced surveillance\intern\weak7\scaler.pkl')
label_encoders = joblib.load(r'C:\Users\mohsa\Downloads\ai\advanced surveillance\intern\weak7\label_encoders.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    weather = request.form['weather']
    car_condition = request.form['car_condition']
    traffic_condition = request.form['traffic_condition']
    distance = float(request.form['distance'])
    jfk_dist = float(request.form['jfk_dist'])
    ewr_dist = float(request.form['ewr_dist'])
    lga_dist = float(request.form['lga_dist'])
    nyc_dist = float(request.form['nyc_dist'])
    bearing = float(request.form['bearing'])

    # Encode categorical variables
    weather_enc = label_encoders['Weather'].transform([weather])[0]
    car_condition_enc = label_encoders['CarCondition'].transform([car_condition])[0]
    traffic_condition_enc = label_encoders['Traffic Condition'].transform([traffic_condition])[0]

    # Create feature array
    features = np.array([[weather_enc, car_condition_enc, traffic_condition_enc, distance, jfk_dist, ewr_dist, lga_dist, nyc_dist, bearing]])
    
    # Scale the features
    scaled_features = scaler.transform(features)
    
    # Predict using the model
    prediction = model.predict(scaled_features)

    return render_template('index.html', prediction_text=f'Estimated Fare: ${prediction[0]:.2f}')

if __name__ == "__main__":
    app.run(debug=True)
