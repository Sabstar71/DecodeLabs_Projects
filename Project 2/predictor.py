import joblib
import pandas as pd


# -----------------------------
# Load Saved Model
# -----------------------------

model = joblib.load("model/car_model.pkl")

encoders = joblib.load("model/label_encoders.pkl")


# -----------------------------
# Predict Function
# -----------------------------

def predict_car(
    buying,
    maint,
    doors,
    persons,
    lug_boot,
    safety,
):

    data = pd.DataFrame(
        [[
            buying,
            maint,
            doors,
            persons,
            lug_boot,
            safety,
        ]],
        columns=[
            "buying",
            "maint",
            "doors",
            "persons",
            "lug_boot",
            "safety",
        ],
    )

    # Encode Input

    for column in data.columns:

        encoder = encoders[column]

        data[column] = encoder.transform(data[column])

    # Prediction

    prediction = model.predict(data)[0]

    # Decode Output

    result = encoders["class"].inverse_transform([prediction])[0]

    return result
