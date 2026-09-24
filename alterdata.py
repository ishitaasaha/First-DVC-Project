import pandas as pd
data = pd.read_csv("Salary_Data.csv")

#print(data.head)

data["YearsExperience"] = 2*data["YearsExperience"]
data.to_csv("Salary_Data.csv",index=False)