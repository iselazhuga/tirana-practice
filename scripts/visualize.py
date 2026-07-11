import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/apartments.csv")

# 1. Histogram i çmimeve
plt.figure(figsize=(8, 5))
plt.hist(df["price"], bins=10, color="steelblue", edgecolor="black")
plt.title("Shpërndarja e Çmimeve të Apartamenteve")
plt.xlabel("Çmimi (EUR)")
plt.ylabel("Numri i Apartamenteve")
plt.tight_layout()
plt.savefig("output/price_distribution.png")
plt.close()

# 2. Bar chart: çmimi mesatar sipas numrit të dhomave
avg_by_bedrooms = df.groupby("bedrooms")["price"].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_by_bedrooms.index, avg_by_bedrooms.values, color="teal", edgecolor="black")
plt.title("Çmimi Mesatar sipas Numrit të Dhomave")
plt.xlabel("Numri i Dhomave (bedrooms)")
plt.ylabel("Çmimi Mesatar (EUR)")
plt.tight_layout()
plt.savefig("output/avg_price_by_bedrooms.png")
plt.close()

print("U ruajtën dy grafikët në output/:")
print("- price_distribution.png")
print("- avg_price_by_bedrooms.png")
# 3. Scatter plot: çmimi kundrejt sipërfaqes (sqm)
plt.figure(figsize=(8, 5))
plt.scatter(df["sqm"], df["price"], color="darkorange", edgecolor="black", alpha=0.7)
plt.title("Çmimi kundrejt Sipërfaqes (m²)")
plt.xlabel("Sipërfaqja (m²)")
plt.ylabel("Çmimi (EUR)")
plt.tight_layout()
plt.savefig("output/price_vs_sqm.png")
plt.close()
print("U ruajtën tre grafikët në output/:")
print("- price_distribution.png")
print("- avg_price_by_bedrooms.png")
print("- price_vs_sqm.png")
# 4. Boxplot: shpërndarja e çmimit sipas numrit të dhomave
plt.figure(figsize=(8, 5))
df.boxplot(column="price", by="bedrooms", grid=False,
           patch_artist=True,
           boxprops=dict(facecolor="lightseagreen"))
plt.title("Shpërndarja e Çmimit sipas Numrit të Dhomave")
plt.suptitle("")  # heq titullin automatik të pandas që dublon
plt.xlabel("Numri i Dhomave (bedrooms)")
plt.ylabel("Çmimi (EUR)")
plt.tight_layout()
plt.savefig("output/price_by_bedrooms_boxplot.png")
plt.close()
print("U ruajtën katër grafikët në output/:")
print("- price_distribution.png")
print("- avg_price_by_bedrooms.png")
print("- price_vs_sqm.png")
print("- price_by_bedrooms_boxplot.png")