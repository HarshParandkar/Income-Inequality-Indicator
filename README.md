# Gini Index Predictor

## Overview

This project provides a web application that predicts the Gini Index based on socio-economic indicators. The model is built using various regression techniques and deployed via a Flask web application.

## Project Structure

- `app.py`: Contains the Flask application code.
- `income_inequality_indicator_2_0.py` - Contains the model building code.
- `index.html`: HTML form for user input.
- `dataset.xlsx`: Dataset for the model. Follow this link to download it - https://docs.google.com/spreadsheets/d/10G_CVXG9qV3GztIFQ0WDGniIP4uIaoMT/edit?usp=drive_link&ouid=101673839528144597155&rtpof=true&sd=true
- `best_model.pkl`: Pickle file containing the trained machine learning model. Follow this link to download the pickle file. - https://drive.google.com/file/d/1rQ4ZJhtlGrt9q5zxEebuAeCbYTK7gjQC/view?usp=drive_link
- `requirements.txt`: Lists the Python dependencies for the project.

## Installation

1. **Clone the Repository:**
2. **Install Dependencies using 'pip install -r requirements.txt'**
3. **Run the Flask App using 'python app.py**
4. **Access the Web Application: Open your browser and go to http://127.0.0.1:5000 to see the Gini Index Predictor web application.**

## Usage
- Enter the required socio-economic indicators into the form fields.
- Click the "Predict" button to get the Gini Index prediction.
## Features
- Input socio-economic data through a web form.
- Predict Gini Index using the trained model.
## Model Details
- Model Type: Random Forest Regressor
- Performance Metrics: Mean Squared Error, R2 Score
## License
- This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- The model was developed as part of a hackathon project.
- Special thanks to the contributors and mentors who provided guidance.
