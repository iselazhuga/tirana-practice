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

@app.route("/good-deals")
def good_deals():
    df = pd.read_csv("data/apartments.csv")
    df["price_per_sqm"] = df["price"] / df["sqm"]
    avg_ppsqm = df["price_per_sqm"].mean()
    good_deals_df = df[df["price_per_sqm"] < avg_ppsqm]
    listings = good_deals_df.to_dict(orient="records")
    return render_template("index.html", listings=listings)

if __name__ == "__main__":
    app.run(debug=True)