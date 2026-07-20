import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# ---------------------------------
# Load Dataset
# ---------------------------------

columns = [
    "buying",
    "maint",
    "doors",
    "persons",
    "lug_boot",
    "safety",
    "class"
]

df = pd.read_csv(
    "dataset/car_evaluation.csv",
    names=columns
)

print("\nDataset Preview\n")
print(df.head())


# ---------------------------------
# Encode Categorical Data
# ---------------------------------

encoders = {}

for column in df.columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(df[column])

    encoders[column] = encoder


# ---------------------------------
# Features & Target
# ---------------------------------

X = df.drop("class", axis=1)

y = df["class"]


# ---------------------------------
# Split Dataset
# ---------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------------
# Train Model
# ---------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)


# ---------------------------------
# Predictions
# ---------------------------------

predictions = model.predict(X_test)


# ---------------------------------
# Accuracy
# ---------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nAccuracy : {accuracy*100:.2f}%\n")

print(classification_report(
    y_test,
    predictions
))

print(confusion_matrix(
    y_test,
    predictions
))


# ---------------------------------
# Save Model
# ---------------------------------

os.makedirs(
    "model",
    exist_ok=True
)

joblib.dump(
    model,
    "model/car_model.pkl"
)

joblib.dump(
    encoders,
    "model/label_encoders.pkl"
)

print("\nModel Saved Successfully.")