# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. #test2

import argparse, os, json
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data", type=str, help="input data")
    parser.add_argument("--output_dir", type=str, help="output dir", default="./outputs")
    args = parser.parse_args()
    return args


args = parse_args()
lines = [
    f"Training data path: {args.input_data}",
    f"output dir path: {args.output_dir}"
]
for line in lines:
    print(line)

df = pd.read_csv(args.input_data)

X = df.drop(columns='totalAmount')
y = df['totalAmount']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

with mlflow.start_run():

    run_id = mlflow.active_run().info.run_id
    mlflow.autolog(log_models=False, exclusive=True)
    print('run_id = ', run_id)

    mlflow.log_metric("Training samples", len(X_train))
    mlflow.log_metric("Test samples", len(X_test))

    # fit scikit-learn linear regression model
    model = LinearRegression().fit(X_train, y_train)
    # print the coefficient
    print("model.coef_", model.coef_.astype("str"))

    # evaluate model
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    mlflow.log_metric("mse", mse)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)

    # Finally save the model to the outputs directory for capture
    os.makedirs(os.path.join(args.output_dir, 'models'), exist_ok=True)
    mlflow.sklearn.save_model(model, os.path.join(args.output_dir, 'models'))

    # Plot actuals vs predictions and save the plot within the run
    plt.figure(figsize=(10, 7))

    #scatterplot of y_test and pred
    plt.scatter(y_test, y_pred) 
    plt.plot(y_test, y_test, color='r')

    plt.title('Actual VS Predicted Values (Test set)') 
    plt.xlabel('Actual Values') 
    plt.ylabel('Predicted Values')
    plt.savefig('actuals_vs_predictions.png')
    mlflow.log_artifact("actuals_vs_predictions.png")


metric = {}
metric['run_id'] = run_id
metric['RMSE'] = rmse
metric['R2'] = r2
print(metric)

with open(os.path.join(args.output_dir, 'metric.json'), "w") as outfile:
    json.dump(metric, outfile)