
# app.py
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the saved model
with open('lang_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        sentence = request.form['sentence']
        if sentence.strip():
            prediction = model.predict([sentence])[0]
        else:
            prediction = "Please enter a sentence!"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
