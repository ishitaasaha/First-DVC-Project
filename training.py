import pandas as pd
from sklearn.linear_model import LinearRegression

# Load Dataset
data = pd.read_csv("Salary_Data.csv")

# Prepare features and target
X = data[["YearsExperience"]]
y = data["Salary"]

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

#Save model
import joblib
joblib.dump(model, 'model.pkl')