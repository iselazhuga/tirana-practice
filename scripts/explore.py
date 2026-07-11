import pandas as pd

df = pd.read_csv("data/apartments.csv")

print("=" * 50)
print("PARË RRESHTAT E PARË (head)")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("INFORMACION MBI KOLONAT (info)")
print("=" * 50)
print(df.info())

print("\n" + "=" * 50)
print("STATISTIKA PËRMBLEDHËSE (describe)")
print("=" * 50)
print(df.describe())