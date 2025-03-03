# FIT-sDNA-DNA-CA Prediction System

This is a Flask-based web application for predicting colorectal cancer (CRC) and Crohn's disease (CD) using a machine learning model. The system takes various biological markers as input and provides prediction results.

**Warning:** This is a development model and is for testing purposes only. Do not use it in clinical diagnosis!!!

## Project Structure

```
.
├── app.py                # Main Flask application
├── PR1_prediction_results_20241127171144.pkl  # Trained model
├── test.xlsx             # Test data
├── requirements.txt      # Python dependencies
├── static/               # Static files
│   ├── script.js         # JavaScript for frontend
│   └── style.css         # CSS styles
└── templates/            # HTML templates
    └── index.html        # Main page template
```

## Requirements

- Python 3.7+
- Flask==2.3.2
- numpy==1.24.4
- pandas==2.0.3
- scikit-learn==1.3.0
- openpyxl==3.1.2

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/flask-prediction-system.git
   cd flask-prediction-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Prepare the model file:
   - Ensure `PR1_prediction_results_20241127171144.pkl` exists in the root directory
   - If needed, retrain the model using your training data

## Running the Application

1. Set environment variables:
   ```bash
   # Windows
   set FLASK_APP=app.py
   set FLASK_ENV=development
   
   # macOS/Linux
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

2. Run the application:
   ```bash
   flask run
   ```

3. Access the application:
   Open your browser and visit:
   ```
   http://localhost:5000
   ```

## API Documentation

### GET /parameters
Returns the default parameters for prediction

Response:
```json
{
  "parameters": {
    "1. Sex(Male=1, Female=0)": 0,
    "2. Age": 59,
    "3. FC": 15,
    "4. FIT(Positive=1, Negative=0)": 1,
    "5. KRAS(Positive= Ct value, Negative=0)": 0,
    "6. BMP3(Positive= Ct value, Negative=0)": 38,
    "7. NDRG4(Positive= Ct value, Negative=0)": 29,
    "8. SDC2(Positive= Ct value, Negative=0)": 0
  }
}
```

### POST /predict
Accepts input features and returns prediction result

Request Body:
```json
{
  "features": [0, 59, 15, 1, 0, 38, 29, 0]
}
```

Response:
```json
{
  "prediction": 0.75,
  "parameters": {
    // same as GET /parameters response
  }
}
```

## Testing

To test the application:
1. Run the Flask development server
2. Use the web interface or API to verify predictions

## Deployment

For production deployment:
1. Install gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Run with gunicorn:
   ```bash
   gunicorn --workers 4 --bind 0.0.0.0:5000 app:app
   ```

3. Configure a reverse proxy (e.g., Nginx) if needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Important Notes

1. This is a research prototype and should not be used for clinical diagnosis
2. Ensure proper data privacy and security measures are in place
3. Regularly update dependencies and security patches
4. Maintain proper logging and monitoring in production
