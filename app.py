import pickle
from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)

# Load your saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    weight = float(request.form['Weight'])
    length1 = float(request.form['Length1'])
    length2 = float(request.form['Length2'])
    length3 = float(request.form['Length3'])
    height = float(request.form['Height'])
    width = float(request.form['Width'])

    # Prepare data for the model (ensure it matches your training data format)
    data = [[weight, length1, length2, length3, height, width]] 
    print(data)

    # Make a prediction
    prediction = model.predict(data)[0]
    print('prediction:',prediction)

    # Return the prediction as a result
    # return render_template('index.html', predicted_species=f'Predicted Species: {prediction}')
    return redirect(url_for('result', prediction=prediction))

@app.route('/result')
def result():
    prediction = request.args.get('prediction')  # Get prediction from URL
    return render_template('result.html', predicted_species=prediction)


if __name__ == '__main__':
    app.run(debug=True) 