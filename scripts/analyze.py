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
# Krijo raport përmbledhës në output/summary.txt
best_deal = df.nsmallest(1, "price_per_sqm").iloc[0]

with open("output/summary.txt", "w", encoding="utf-8") as f:
    f.write("RAPORT PËRMBLEDHËS — TIRANA APARTMENT SCOUT\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Numri total i shpalljeve: {len(df)}\n")
    f.write(f"Çmimi mesatar: {df['price'].mean():,.0f} EUR\n")
    f.write(f"Sipërfaqja mesatare: {df['sqm'].mean():.1f} m²\n\n")
    f.write("OFERTA MË E MIRË (çmimi më i ulët për m²):\n")
    f.write(f"  Lagjja: {best_deal['neighborhood']}\n")
    f.write(f"  Çmimi: {best_deal['price']:,.0f} EUR\n")
    f.write(f"  Sipërfaqja: {best_deal['sqm']} m²\n")
    f.write(f"  Dhoma gjumi: {best_deal['bedrooms']}\n")
    f.write(f"  Çmimi/m²: {best_deal['price_per_sqm']:.2f} EUR/m²\n")

print("U ruajt raporti në output/summary.txt")