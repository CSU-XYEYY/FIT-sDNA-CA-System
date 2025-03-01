# Flask Web Application

This is a Flask web application for displaying prediction results.

## Project Structure

```
.
├── app.py                # Main Flask application
├── PR1_prediction_results_20241127171144.pkl  # Prediction results data
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
- Flask
- Other dependencies (if any)

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Set up the environment:
   ```bash
   set FLASK_APP=app.py
   set FLASK_ENV=development
   ```
2. Run the application:
   ```bash
   flask run
   ```
3. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
