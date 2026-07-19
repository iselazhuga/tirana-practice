from flask import Flask, render_template
import pandas as pd
import joblib

app = Flask(__name__)
NEIGHBORHOOD_COORDS = {
    "Bllok": (41.3231, 19.8172),
    "Don Bosko": (41.3105, 19.7959),
    "Kombinat": (41.2990, 19.7775),
    "Fresk": (41.3400, 19.8100),
    "Yzberisht": (41.3350, 19.7600),
    "Selitë": (41.3450, 19.8250),
    "Astir": (41.3600, 19.8400),
    "Ali Demi": (41.3150, 19.8300),
    "Laprakë": (41.3300, 19.7700),
    "Njësia 5": (41.3250, 19.8150),
    "21 Dhjetori": (41.3280, 19.8200),
    "Liqeni i Thatë": (41.3500, 19.8000),
}

TIRANA_CENTER = (41.3275, 19.8187)

def get_coordinates(neighborhood):
    return NEIGHBORHOOD_COORDS.get(neighborhood, TIRANA_CENTER)

@app.route("/")
def home():
    df = pd.read_csv("data/apartments.csv")
    listings = df.to_dict(orient="records")
    return render_template("index.html", listings=listings)

@app.route("/listing/<int:listing_id>")
def listing_detail(listing_id):
    df = pd.read_csv("data/apartments.csv")
    listing = df.iloc[listing_id].to_dict()

    model = joblib.load("models/price_model.joblib")
    features = pd.DataFrame([{
        "sqm": listing["sqm"],
        "bedrooms": listing["bedrooms"],
        "bathrooms": listing["bathrooms"],
        "floor": listing["floor"]
    }])
    predicted_price = model.predict(features)[0]

    return render_template("listing.html", listing=listing, predicted_price=predicted_price)

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