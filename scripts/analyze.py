import pandas as pd

df = pd.read_csv("data/apartments.csv")

# Shto kolonën price_per_sqm
df["price_per_sqm"] = df["price"] / df["sqm"]

print("=" * 50)
print("ÇMIMI MESATAR SIPAS NUMRIT TË DHOMAVE")
print("=" * 50)
avg_by_bedrooms = df.groupby("bedrooms")["price"].mean()
print(avg_by_bedrooms)

print("\n" + "=" * 50)
print("3 OFERTAT MË TË MIRA (çmimi më i ulët për m²)")
print("=" * 50)
best_deals = df.nsmallest(3, "price_per_sqm")
print(best_deals)