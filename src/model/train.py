import argparse
import os

import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def parse_args():
    # 引数の処理
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data", type=str, help="input data")
    parser.add_argument(
        "--output_dir", type=str, help="output dir", default="./outputs"
    )
    args = parser.parse_args()
    return args


def process_data(df):
    # X, y の作成
    X = df.drop(columns="totalAmount")
    y = df["totalAmount"]

    # 学習データ、テストデータの分割
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=0
    )

    # 分割データの出力
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    # データのサンプル数のロギング
    mlflow.log_metric("Train samples", len(X_train))

    # モデル学習
    model = LinearRegression().fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):
    # データのサンプル数のロギング
    mlflow.log_metric("Test samples", len(X_test))

    # モデル評価
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # 精度メトリックのロギング
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2", r2)

    # 実測値と予測値のプロット
    plot_actuals_predictions(y_test, y_pred)


def plot_actuals_predictions(y_test, y_pred):
    # 実測値と予測値のプロット
    plt.figure(figsize=(10, 7))
    plt.scatter(y_test, y_pred)
    plt.plot(y_test, y_test, color="r")
    plt.title("Actual VS Predicted Values (Test set)")
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.savefig("actuals_vs_predictions.png")

    # プロット画像のロギング
    mlflow.log_artifact("actuals_vs_predictions.png")


def save_model(model, output_dir):
    # モデルの保存
    os.makedirs(os.path.join(output_dir, "models"), exist_ok=True)
    mlflow.sklearn.save_model(model, os.path.join(output_dir, "models"))


def main(args):
    # 自動ロギングの有効化
    mlflow.autolog(log_models=False)

    # 引数の確認
    lines = [
        f"学習データのパス: {args.input_data}",
        f"出力フォルダのパス: {args.output_dir}",
    ]
    [print(line) for line in lines]

    # 学習データの読み込み
    df = pd.read_csv(args.input_data)

    # データ前処理
    X_train, X_test, y_train, y_test = process_data(df)

    # モデル学習
    model = train_model(X_train, y_train)

    # モデル評価
    evaluate_model(model, X_test, y_test)

    # モデル保存
    dir = os.path.join(args.output_dir, os.environ["AZUREML_RUN_ID"])
    save_model(model, dir)


if __name__ == "__main__":
    # 引数の処理
    args = parse_args()

    # main 関数の実行
    main(args)
