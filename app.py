from flask import Flask, render_template, request
import joblib
import numpy as np

model, target_names = joblib.load("svm_iris_model.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            values = [
                float(request.form["sepal_length"]),
                float(request.form["sepal_width"]),
                float(request.form["petal_length"]),
                float(request.form["petal_width"])
            ]
            pred_class = model.predict([values])[0]
            pred_proba = model.predict_proba([values])[0]
            prediction = {
                "class": target_names[pred_class].capitalize(),
                "confidence": round(max(pred_proba) * 100, 2)
            }
        except:
            prediction = "Invalid input"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
