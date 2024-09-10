from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load the model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from form data
    try:
        feature1 = float(request.form.get('feature1'))
        feature2 = float(request.form.get('feature2'))
        # Add more features as needed

        # Prepare features for prediction
        features = [feature1, feature2]  # Adjust according to your feature names
        prediction = model.predict([features])

        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
