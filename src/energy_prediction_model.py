
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("ml_energy_dataset.csv")

X = data[["hour","temperature"]]
y = data["energy_kwh"]

model = LinearRegression()
model.fit(X,y)

prediction = model.predict(X)

print("Predicted energy values:", prediction)
