import joblib
import pandas as pd

# Ngarko modelin e ruajtur
model = joblib.load("models/price_model.joblib")

# Apartament i trilluar
apartment = pd.DataFrame([{
    "sqm": 75,
    "bedrooms": 2,
    "bathrooms": 1,
    "floor": 3
}])

# Bëj parashikimin
predicted_price = model.predict(apartment)[0]

print(f"Çmimi i parashikuar: {predicted_price:,.2f} EUR")