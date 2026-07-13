import pandas as pd
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

import joblib

# Ruaj modelin e trajnuar
joblib.dump(model, "models/price_model.joblib")
print("Modeli u ruajt te models/price_model.joblib")