from flask import Flask, request, render_template, jsonify
import numpy as np
import joblib
import pandas as pd
import pickle

app = Flask(__name__)

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Route for displaying input form
@app.route('/', methods=['GET'])
def input_form():
    return render_template('input_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect the planned delivery days
        planned_delivery = int(request.form.get('Planned Delivery'))

        # Map the selected "Day of Week" to binary features
        day_of_week = request.form.get('Day Of Week')
        M_W_F = 1 if day_of_week == 'M_W_F' else 0
        T_T_S = 1 if day_of_week == 'T_T_S' else 0
        Sunday = 1 if day_of_week == 'Sunday' else 0

        # Map the selected "Weather Condition" to binary features
        weather_condition = request.form.get('Weather Condition')
        weather_clear = 1 if weather_condition == 'Clear Weather' else 0
        weather_disturbed = 1 if weather_condition == 'Disturbed Weather' else 0

        # Map the selected "Vehicle Type" to binary features
        vehicle_type = request.form.get('Vehicle Type')
        vehicle_container = 1 if vehicle_type == 'Vehicle Type_Container' else 0
        vehicle_lorry = 1 if vehicle_type == 'Vehicle Type_Lorry' else 0
        vehicle_trailer = 1 if vehicle_type == 'Vehicle Type_Trailer' else 0
        vehicle_truck = 1 if vehicle_type == 'Vehicle Type_Truck' else 0

        # Map the selected "Traffic Condition" to binary features
        traffic_condition = request.form.get('Traffic Condition')
        traffic_heavy = 1 if traffic_condition == 'Traffic Conditions_Heavy' else 0
        traffic_light = 1 if traffic_condition == 'Traffic Conditions_Light' else 0
        traffic_moderate = 1 if traffic_condition == 'Traffic Conditions_Moderate' else 0

        # Map the selected "Distance Type" to binary features
        distance_type = request.form.get('Distance Type')
        distance_short = 1 if distance_type == 'Short' else 0
        distance_medium = 1 if distance_type == 'Medium' else 0
        distance_large = 1 if distance_type == 'Large' else 0

        # Create DataFrame with consistent column names
        df = pd.DataFrame({
            'Planned Delivery (in days)': [planned_delivery],
            'M_W_F': [M_W_F],
            'T_T_S': [T_T_S],
            'Sunday': [Sunday],
            'Clear Weather': [weather_clear],
            'Disturbed Weather': [weather_disturbed],
            'Vehicle Type_Container': [vehicle_container],
            'Vehicle Type_Lorry': [vehicle_lorry],
            'Vehicle Type_Trailer': [vehicle_trailer],
            'Vehicle Type_Truck': [vehicle_truck],
            'Traffic Conditions_Heavy': [traffic_heavy],
            'Traffic Conditions_Light': [traffic_light],
            'Traffic Conditions_Moderate': [traffic_moderate],
            'Distance Type_Large': [distance_short],
            'Distance Type_Medium': [distance_medium],
            'Distance Type_Short': [distance_large]
        })

        # Predict using the trained model
        prediction = model.predict(df)
        print(f"Prediction: {prediction}")

        # Render result page with prediction
        return render_template('prediction_result.html', prediction=prediction[0])

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 400

if __name__ == '__main__':
    app.run(debug=True)
