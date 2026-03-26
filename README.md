-> AI-based Diabetes Risk Predictor
An AI-powered command line tool that predicts whether a person is at high risk of diabetes based on basic health parameters like age, BMI, glucose level, etc.

Disclaimer:
This project is for educational purposes only and not a medical diagnostic tool.
For medical advice, always consult a qualified doctor.

Project Overview
This project uses a Machine Learning classification model to predict diabetes risk.
The user enters health-related values through the terminal, the model processes these inputs, and outputs whether the user is “Likely Diabetic” or “Not Likely Diabetic”.

The project demonstrates:

Basic ML pipeline (data loading → training → prediction)
Usage of scikit-learn for classification
Simple and clear CLI-based user interaction
Functional Requirements (Modules)
As per project guideline, we have at least 3 major functional modules :contentReference[oaicite:1]{index=1}:

Data & Model Module

Load dataset (e.g., sample diabetes dataset – CSV file)
Split data into train/test
Train a Machine Learning model (e.g., Logistic Regression / RandomForest)
Save/Use trained model for prediction
Input & Preprocessing Module

Take user input from CLI:
Age
BMI
Glucose level
Blood pressure
Number of pregnancies (optional)
Convert and scale/normalize values if required
Prediction & Output Module

Pass processed input to the trained model
Get prediction: 0 = Not Likely Diabetic, 1 = Likely Diabetic
Show user-friendly message:
“You are at high risk of diabetes. Please consult a doctor.”
or “You are at low risk based on the model.”
Non-Functional Requirements
At least 4 NFRs as required in the document :contentReference[oaicite:2]{index=2}:

Usability:
Simple question-answer style CLI. Clear instructions and prompts.

Performance:
Small dataset + lightweight ML model → fast predictions in under a second.

Reliability & Robustness:

Input validation (check for non-numeric / negative values)
Basic error handling using try-except
Maintainability:

Code divided into functions: train_model(), get_user_input(), predict_risk()
Easy to change model or add new features
Privacy (Optional NFR):
User data is not stored permanently; only used in runtime for prediction.

System Architecture (High-Level)

```text
          ┌────────────────────┐
          │   User Input (CLI) │
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │ Preprocessing Layer│
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │  ML Model (Classifier)
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │  Risk Prediction    │
          └─────────┬──────────┘
                    │
          ┌─────────▼──────────┐
          │  Result to User     │
          └─────────────────────┘
