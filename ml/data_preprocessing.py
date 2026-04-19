import pandas as pd
import pickle

df = pd.read_csv("../data/train.csv")

# watch the data
print(df.head())
# watch related info
print(df.info())
# watch summary
print(df.describe())

# target
y = df["SalePrice"]
# remove target from features
x = df.drop("SalePrice", axis=1)

print("x shape: ", x.shape)
print("y shape: ", y.shape)

# check missing values
print(df.isnull().sum().sort_values(ascending=False).head(20))

# handle missing values
for col in x.columns:
    if x[col].dtype == "object":
        x[col] = x[col].fillna("None")
    else:
        x[col] = x[col].fillna(x[col].median())

# encode categorical variables (object -> numeric)
x = pd.get_dummies(x)

print("x shape after encoding: ", x.shape)

# align data
pickle.dump(x.columns, open("../data/columns.pkl", "wb"))

# last check
print(x.isnull().sum().sum())

# save cleaned data
x.to_csv("../data/x_cleaned.csv", index=False)
y.to_csv("../data/y_cleaned.csv", index=False)