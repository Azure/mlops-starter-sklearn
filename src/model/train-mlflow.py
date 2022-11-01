import mlflow
import argparse
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import (
    train_test_split,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_squared_error,
    r2_score,
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input_data",
    type=str,
    help="input data",
)

args = parser.parse_args()

lines = [f"Training data path: {args.input_data}"]
[print(line) for line in lines]

mlflow.sklearn.autolog()

df = pd.read_csv(args.input_data)


X = df.drop(columns="totalAmount")
y = df["totalAmount"]
(
    X_train,
    X_test,
    y_train,
    y_test,
) = train_test_split(
    X, y, test_size=0.30, random_state=0
)


model = LinearRegression().fit(X_train, y_train)

model.coef_  # 探索目的のコード


y_test_pred = model.predict(X_test)
print(mean_squared_error(y_test, y_test_pred))
print(r2_score(y_test, y_test_pred))


plt.scatter(
    y_test_pred,
    y_test_pred - y_test,
    marker="o",
    color="blue",
)
plt.hlines(
    y=0,
    xmin=-30,
    xmax=100,
    linewidth=3,
    color="orange",
)
plt.show()

plt.savefig("outputs/residual_plot.png")

mlflow.log_artifact("outputs/residual_plot.png")
