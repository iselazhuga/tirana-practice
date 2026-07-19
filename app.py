from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("data/apartments.csv")
    listings = df.to_dict(orient="records")
    return render_template("index.html", listings=listings)

@app.route("/listing/<int:listing_id>")
def listing_detail(listing_id):
    df = pd.read_csv("data/apartments.csv")
    listing = df.iloc[listing_id].to_dict()
    return render_template("listing.html", listing=listing)

if __name__ == "__main__":
    app.run(debug=True)