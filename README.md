# Shipment Delay Prediction Model

## Project Overview

Timely deliveries are crucial in freight logistics. This project aims to predict whether a shipment will be delayed or arrive on time based on historical data. The goal is to build a classification model, experiment with different machine learning algorithms, and deploy the model through a web-based API.

## Approach

### 1. Data Preparation & Exploration
- Cleaned the dataset by handling missing values and outliers.
- Performed basic exploratory data analysis (EDA) to better understand the dataset and identify useful features that could help in predicting shipment delays.
- Drew conclusions from the dataset to identify the most important factors influencing shipment timeliness, such as weather, traffic, and distance.

### 2. Feature Engineering
- Engineered relevant features based on the dataset, including:
  - Weather conditions
  - Traffic levels
  - Distance between origin and destination
  - Vehicle type
  - And other shipment-related details

### 3. Model Development
- **Model Selection:** Chose **Decision Tree Classifier** as the model for prediction. The decision tree is a strong candidate for this classification task because:
  - It can handle both categorical and continuous data.
  - It provides interpretability, which helps in understanding the contribution of each feature to the prediction.
  - It is effective for datasets with a mix of feature types and has good performance for small to medium-sized datasets.
  
- **Training Accuracy:** 94.41%
- **Testing Accuracy:** 94.65%

### 4. Deployment
- Developed a simple web-based API using **Flask**.
- The API accepts shipment details such as:
  - Origin
  - Destination
  - Vehicle type
  - Distance
  - Weather conditions
  - Traffic levels
- The API returns a prediction indicating whether the shipment will be "Delayed" or "On Time".

## How to Run the Project

### 1. Install Dependencies
Ensure you have all necessary dependencies by installing them from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 2. Run the Flask App
To start the Flask app and access the API, run the following command in the terminal:

```bash
flask run --reload
```

This will start a local development server, and you can access the web-based portal in your browser.

### 3. Access the Web API
-Once the Flask app is running, you can send requests to the API by providing shipment details (origin, destination, vehicle type, distance, weather, traffic) and get a prediction (Delayed or On Time).

### Conclusion
This project demonstrates the ability to handle data, train a classification model, and deploy it into a web API for shipment delay prediction. The Decision Tree Classifier performed well, and the project provides a foundation for further improvement with more complex models or additional features.


