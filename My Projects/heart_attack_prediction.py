# -*- coding: utf-8 -*-
"""Heart_Attack_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P391P7cDmwmEWL1TO8eJ0Qy2zL89diSe

# **HEART ATTACK PREDICTION USING SVM**
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, roc_auc_score

data = pd.read_csv("/content/heart.csv")

data.info

data.head()

features = ["age", "sex", "cp", "trtbps","chol","fbs","restecg","thalachh","exng","oldpeak","slp","caa","thall","output"]  # Replace with actual features
target = "output"

X = data[features]
y = data[target]

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = le.fit_transform(X[col])


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = SVC(kernel="rbf")


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


new_data = pd.DataFrame({
    "age": [54],
    "sex": [0],
    "cp": [2],
    "trtbps": [135],
    "chol":[240],
    "fbs":[1],
    "restecg":[1],
    "thalachh":[150],
    "exng":[0],
    "oldpeak":[2.1],
    "slp":[2],
    "caa":[0],
    "thall":[2],
    "output":[0]
})

for col in new_data.columns:
    if new_data[col].dtype == 'object':
        new_data[col] = le.transform(new_data[col])

new_data_scaled = scaler.transform(new_data)

predicted_heart_attack = model.predict(new_data_scaled)[0]
print("Predicted heart attack:", predicted_heart_attack)