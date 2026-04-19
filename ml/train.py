import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

x = pd.read_csv("../data/x_cleaned.csv")
y = pd.read_csv("../data/y_cleaned.csv")

# convert to series (y now is a dataframe, need to convert to series)
y = y.values.ravel()

print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(n_estimators=100)
}

results = {}

for name, model in models.items():
    model.fit(x_train, y_train)
    preds = model.predict(x_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    results[name] = rmse

    print(f"{name} RMSE: {rmse}")

best_model_name = min(results, key=results.get)
best_model = models[best_model_name]

print("Best model:", best_model_name)

# save the best model
pickle.dump(best_model, open("../backend/model.pkl", "wb"))

sample = x_test.iloc[0:1]
pred = best_model.predict(sample)

print("Prediction:", pred)
print("Actual:", y_test[0])