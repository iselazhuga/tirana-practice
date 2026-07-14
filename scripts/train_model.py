import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# Ngarko të dhënat
df = pd.read_csv("data/apartments.csv")

# Features (X) dhe target (y)
X = df[["sqm", "bedrooms", "bathrooms", "floor"]]
y = df["price"]

# Ndaj në train dhe test (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Trajno modelin
model = LinearRegression()
model.fit(X_train, y_train)

# Bëj parashikime mbi test set-in
predictions = model.predict(X_test)

# Vlerëso modelin
r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print(f"R² score: {r2:.3f}")
print(f"Mean Absolute Error: {mae:,.2f} EUR")

# Trajno edhe një Random Forest për krahasim
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

rf_r2 = r2_score(y_test, rf_predictions)
rf_mae = mean_absolute_error(y_test, rf_predictions)

print(f"\nRandom Forest R² score: {rf_r2:.3f}")
print(f"Random Forest Mean Absolute Error: {rf_mae:,.2f} EUR")

import joblib

# Ruaj modelin e trajnuar
joblib.dump(model, "models/price_model.joblib")
print("Modeli u ruajt te models/price_model.joblib")
# Grafik: çmimet reale vs të parashikuara (Linear Regression)
plt.figure(figsize=(8, 6))
plt.scatter(y_test, predictions, color="steelblue", edgecolor="black", alpha=0.7)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red", linestyle="--", label="Parashikim perfekt"
)
plt.title("Çmimi Real vs Çmimi i Parashikuar")
plt.xlabel("Çmimi Real (EUR)")
plt.ylabel("Çmimi i Parashikuar (EUR)")
plt.legend()
plt.tight_layout()
plt.savefig("output/predicted_vs_actual.png")
plt.close()

print("U ruajt grafiku te output/predicted_vs_actual.png")