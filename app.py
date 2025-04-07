from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model (handling dict if needed)
with open("model (3).pkl", "rb") as f:
    model_data = pickle.load(f)
    model = model_data['model'] if isinstance(model_data, dict) else model_data

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            features = [
                float(request.form['open']),
                float(request.form['high']),
                float(request.form['low']),
                float(request.form['close']),
                float(request.form['adj_close']),
                float(request.form['volume']),
                float(request.form['sentiment_score']),
                float(request.form['score']),
                float(request.form['target'])
            ]
            prediction = model.predict([features])[0]
            return render_template("result.html", prediction=prediction)
        except Exception as e:
            return render_template("result.html", prediction=f"Error: {str(e)}")
    else:
        return render_template("predict.html")

if __name__ == '__main__':
    app.run(debug=True)
