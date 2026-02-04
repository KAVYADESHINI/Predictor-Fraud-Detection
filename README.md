🏥**Healthcare provider Fraud Detection System**

An end-to-end **Machine Learning project** to detect **fraudulent healthcare providers** by analyzing large-scale insurance claims data.
The system helps identify potential **Fraud, Waste, and Abuse** (FWA) using supervised learning models and is deployed as an interactive web application.

🔗**GitHub Repository**: https://github.com/KAVYADESHINI/Predictor-Fraud-Detection

📌 **Problem Statement**

Healthcare fraud leads to massive **financial losses** and reduced **trust** in healthcare systems.
The goal of this project is to **classify healthcare providers as fraudulent or non-fraudulent** by learning patterns from historical insurance claims data.

📊 **Dataset Description**

The project uses public healthcare insurance claims data, integrating information from:
Provider details
Inpatient claims
Outpatient claims
Beneficiary data

📈 **Scale:**

500,000+ insurance claim records
Highly imbalanced dataset (fraud cases are rare)

🧠 **Approach & Methodology**
1️⃣**Data Integration**
Merged multiple datasets using provider-level keys
Aggregated claims to create a provider-centric view

2️⃣ **Feature Engineering**
Created meaningful features such as:
Total claim count per provider
Total reimbursement amount
Deductible and co-pay amounts
Inpatient vs outpatient claim ratios

3️⃣ **Exploratory Data Analysis (EDA)**
Analyzed fraud vs non-fraud distributions
Identified key financial indicators correlated with fraud

4️⃣ **Model Building**
Implemented and compared:
Logistic Regression
Random Forest Classifier

5️⃣ **Model Evaluation**
Used fraud-sensitive metrics:
Precision
Recall
F1-score
ROC-AUC (Achieved **0.93**)
🔧 Threshold tuning was applied to improve fraud **recall** to **~75%***, prioritizing detection of fraudulent providers.

🚀**Deployment**

Built an interactive Streamlit web application
Serialized trained model using Pickle
Enables real-time fraud risk prediction for providers

🛠️ **Tech Stack**
**Programming & Libraries**
Python
Pandas, NumPy
Scikit-learn
TensorFlow 
Streamlit
Machine Learning
Classification models
Feature engineering
Threshold tuning
Model evaluation (ROC-AUC, Confusion Matrix)

**Tools**
Git & GitHub
Pickle (model serialization)

📂 **Project Structure**
**Predictor-Fraud-Detection**/
│
├── data/                  # Raw and processed datasets
├── notebooks/             # EDA and model development notebooks
├── app.py                 # Streamlit application
├── model.pkl              # Serialized trained model
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

📈 **Key Results**
ROC-AUC Score: 0.93
Improved fraud recall to ~75%
Successfully deployed a usable ML application

🌟 **Key Learnings**
Handling imbalanced datasets in real-world ML problems
Importance of feature engineering over model complexity
Selecting business-driven evaluation metrics
Deploying ML models for practical usage

🔮 **Future Improvements**
Add advanced anomaly detection techniques
Experiment with ensemble and boosting models
Implement MLOps practices (CI/CD, model monitoring)
Improve UI and add explainability (SHAP values)

👩‍💻**Author**
Kavya Deshini
Entry-Level Machine Learning Engineer
📧 Email: kavyadeshini1224@gmail.com

🔗 GitHub: https://github.com/KAVYADESHINI
