# diabetes_predictor.py

"""
AI-based Diabetes Risk Predictor (Educational Project)

NOTE:
- This is a toy ML model trained on a VERY small dummy dataset.
- It is ONLY for learning and college project submission.
- It is NOT a medical diagnostic tool.
"""

from sklearn.linear_model import LogisticRegression
import numpy as np

def train_model():
    """
    Dummy training data:
    Features: [glucose, bmi, age, blood_pressure]
    Label: 0 = Low Risk, 1 = High Risk
    """

    # Very small made-up dataset (just for demo)
    X = np.array([
        [110, 22, 25, 75],   # low risk
        [95,  20, 21, 70],   # low risk
        [130, 28, 35, 82],   # high risk
        [145, 32, 45, 90],   # high risk
        [160, 35, 50, 95],   # high risk
        [105, 23, 27, 72],   # low risk
        [120, 26, 30, 78],   # medium-ish
        [170, 38, 55, 98],   # very high
    ])

    y = np.array([
        0,  # low
        0,
        1,  # high
        1,
        1,
        0,
        1,
        1
    ])

    model = LogisticRegression()
    model.fit(X, y)
    return model

def get_user_input():
    print("Please enter the following details:")
    while True:
        try:
            glucose = float(input("Glucose level (mg/dL): "))
            bmi = float(input("BMI (e.g., 24.5): "))
            age = int(input("Age (years): "))
            bp = float(input("Blood Pressure (mmHg): "))
            if glucose <= 0 or bmi <= 0 or age <= 0 or bp <= 0:
                print("Values must be positive. Please try again.\n")
                continue
            return [glucose, bmi, age, bp]
        except ValueError:
            print("Invalid input! Please enter numeric values only.\n")

def predict_risk(model, features):
    # features is a list [glucose, bmi, age, bp]
    X_input = np.array(features).reshape(1, -1)
    prediction = model.predict(X_input)[0]
    prob = model.predict_proba(X_input)[0][1]  # probability of high risk (class 1)
    return prediction, prob

def main():
    print("==============================================")
    print("    AI-based Diabetes Risk Predictor (Demo) ")
    print("==============================================")
    print("Disclaimer: This is NOT a medical tool. It is")
    print("only for educational/project use.\n")

    # Train model once
    model = train_model()

    while True:
        user_features = get_user_input()
        pred, prob = predict_risk(model, user_features)

        print("\n--------- RESULT ---------")
        if pred == 1:
            print("Prediction: HIGH RISK of diabetes.")
        else:
            print("Prediction: LOW RISK based on model.")

        print(f"Model confidence (high-risk probability): {prob * 100:.2f}%")
        print("---------------------------")
        print("NOTE: This result is based on a tiny demo model.")
        print("For real diagnosis, consult a doctor.\n")

        again = input("Do you want to test another person? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using the Diabetes Risk Predictor. Goodbye!")
            break

if __name__ == "__main__":
    main()
