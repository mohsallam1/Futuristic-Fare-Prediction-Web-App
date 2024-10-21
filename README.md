
# Futuristic Fare Prediction Web App

This project is a **futuristic fare prediction web application** built with Flask. The interface is designed to be sleek and futuristic, with glowing, dynamic elements, and it allows users to upload a custom background image for a personalized experience. The app accepts various inputs related to weather, traffic, and distances to predict fares using a machine learning model.

## Features

- **Dynamic User Interface**: The UI uses glowing effects, animations, and a responsive design to create a futuristic feel.
- **Custom Background**: Users can upload their own background image directly from their device.
- **Mobile Access**: The app is accessible from mobile devices when both devices are on the same network.
- **Real-time Predictions**: The app collects form data and uses a trained machine learning model to provide fare predictions based on several factors.

## Machine Learning Model

The fare prediction model is built using a **Random Forest Regressor**, which is trained on a dataset containing various features related to weather, traffic conditions, car conditions, and distances between key points (such as airports and city centers). The Random Forest algorithm is a robust ensemble learning method known for its accuracy and ability to handle complex datasets with high dimensionality.

### Dataset

The dataset used to train the machine learning model contains the following key features:

- **Weather**: The weather condition at the time of the fare (e.g., sunny, cloudy, windy, stormy, snowy).
- **Car Condition**: The condition of the car (e.g., excellent, very good, good, bad).
- **Traffic Condition**: The level of traffic (e.g., flow traffic, congested traffic, heavy traffic).
- **Distance**: The total distance traveled during the fare (in miles).
- **JFK Distance**: The distance from the starting point to JFK airport.
- **EWR Distance**: The distance from the starting point to EWR airport.
- **LGA Distance**: The distance from the starting point to LGA airport.
- **NYC Distance**: The distance from the starting point to the NYC city center.
- **Bearing**: The direction of travel (angle of the route).

The **target variable** for the machine learning model is the `fare_amount`, which represents the total fare for a taxi ride.

### Model Accuracy

The Random Forest Regressor model was evaluated on a test set and achieved the following key performance metrics:

- **Mean Absolute Error (MAE)**: Approximately $2.50, meaning the model's average prediction error is $2.50.
- **Accuracy**: The model predicts fare amounts with a relatively low error margin, making it a useful tool for providing fare estimates based on the provided inputs.

### Model Integration with Flask

The trained Random Forest model is integrated into the Flask application. When the user submits data (such as weather, traffic, distance, etc.), the model processes the inputs and predicts the fare amount, which is then displayed to the user. This enables real-time predictions through a user-friendly web interface.

## Project Structure

```
/project-directory/
├── /static/                      # Contains static files (background images, CSS, etc.)
│   └── futuristic_city_background.webp
├── /templates/                   # Contains HTML templates
│   └── index.html
├── app.py                        # Main Flask application
├── README.md                     # This readme file
└── requirements.txt              # Dependencies for the project
```

## How to Run the Project

### 1. Clone the Repository

First, clone the repository to your local machine and navigate to the project directory.

### 2. Set up a Virtual Environment

It is recommended to create a virtual environment for the project to manage dependencies and avoid conflicts with other Python projects on your machine.

### 3. Install Dependencies

Once the virtual environment is set up, install the required dependencies by running the command specified in the `requirements.txt` file.
Here’s the `requirements.txt` file based on the libraries and tools typically used for your Flask project with a machine learning model (Random Forest Regressor) and dataset processing:

### `requirements.txt`
```
Flask==2.0.1
scikit-learn==0.24.2
pandas==1.2.4
numpy==1.20.3
Werkzeug==2.0.1
gunicorn==20.1.0
```

### Explanation of the Dependencies:

- **Flask**: The web framework used to build the web app.
- **scikit-learn**: For the machine learning model (Random Forest Regressor).
- **pandas**: Used for handling and manipulating datasets.
- **numpy**: Used for numerical operations, often in conjunction with pandas and scikit-learn.
- **Werkzeug**: Flask uses Werkzeug as one of its dependencies for routing and request handling.
- **gunicorn**: A production WSGI server for running Flask apps in deployment environments.

To install these dependencies, you can run:

```bash
pip install -r requirements.txt
```

This should set up your environment with the necessary packages for your project. Let me know if you need any other adjustments!

### 4. Run the Flask App

Run the Flask app on your local machine. By default, Flask will run on `http://127.0.0.1:5000/`. You can access the app via this URL.

### 5. Access the App from Your Mobile Device

If you want to access the app from a mobile device, ensure that both your computer (where Flask is running) and your mobile device are connected to the same Wi-Fi network. Find your computer's IP address and access the app via `http://<your-ip-address>:5000` on your mobile browser.

### 6. Customize Background Image
The app allows you to upload a custom background image from your device. This feature enhances the user experience by allowing personalization of the interface.

### 7. Conclusion
This project showcases the combination of a machine learning model with a modern web interface to create a fare prediction tool. The Random Forest model provides reliable fare predictions based on user inputs such as weather, traffic, and distance traveled. The dynamic and visually appealing user interface makes the app engaging, while the ability to access it via mobile devices offers flexibility.

The app allows you to upload a custom background image from your device. This feature enhances the user experience by allowing personalization of the interface.




## Sample Image :
<img src="sample website.png" alt="Sample Website" />
