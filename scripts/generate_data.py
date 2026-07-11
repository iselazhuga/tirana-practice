import pandas as pd
import random

# Lagje reale të Tiranës për realizëm
neighborhoods = [
    "Bllok", "Don Bosko", "Kombinat", "Fresk", "Yzberisht",
    "Selitë", "Astir", "Ali Demi", "Laprakë", "Njësia 5",
    "21 Dhjetori", "Liqeni i Thatë"
]

random.seed(42)  # rezultate të përsëritshme çdo herë që e xhirosh

rows = []
for _ in range(40):
    sqm = random.randint(40, 160)
    bedrooms = random.randint(1, 4)
    bathrooms = random.randint(1, min(bedrooms, 3))
    floor = random.randint(0, 10)
    neighborhood = random.choice(neighborhoods)

    price_per_sqm = random.randint(900, 1800)
    price = int(sqm * price_per_sqm * random.uniform(0.9, 1.15))

    rows.append({
        "price": price,
        "sqm": sqm,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "floor": floor,
        "neighborhood": neighborhood
    })

df = pd.DataFrame(rows)
df.to_csv("data/apartments.csv", index=False)

print(f"U ruajtën {len(df)} rreshta në data/apartments.csv")