from flask import Flask, request, render_template
import joblib

app = Flask(name)

model = joblib.load("models/phishing_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""

    if request.method == "POST":
        email_text = request.form["email"]

        result = model.predict([email_text])[0]

        prediction = result

    return render_template(
        "index.html",
        prediction=prediction
    )

if name == "main":
    app.run(debug=True)
