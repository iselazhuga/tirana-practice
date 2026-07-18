from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("data/apartments.csv")
    listings = df.to_dict(orient="records")
    return render_template("index.html", listings=listings)

if __name__ == "__main__":
    app.run(debug=True)