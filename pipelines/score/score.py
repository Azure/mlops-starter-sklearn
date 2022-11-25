import argparse
from pathlib import Path

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd


def parse_args():
    # 引数の処理
    parser = argparse.ArgumentParser()
    parser.add_argument("--testing_data", type=str, help="Path of testing data")
    parser.add_argument("--model_input", type=str, help="Path of model input")
    parser.add_argument("--predicted_data", type=str, help="Path of predicted data")
    args = parser.parse_args()
    return args


def split_label(df):
    X = df.drop(columns="totalAmount")
    y = df["totalAmount"]
    return X, y


def get_model(model_input):
    return mlflow.sklearn.load_model(model_input)


def score_model(X_test, model):
    pred = model.predict(X_test)
    return pred


def save_data(pred, predicted_data):
    np.savetxt(Path(args.predicted_data) / "pred.csv", pred, delimiter=",")


def main(args):
    # 引数の確認
    lines = [
        f"testing_data のパス: {args.testing_data}",
        f"モデル入力ファイルのパス: {args.model_input}",
    ]
    [print(line) for line in lines]

    # テストデータの読み込み
    df = pd.read_csv(Path(args.testing_data) / "test.csv")

    # データ前処理
    X_test, y_test = split_label(df)

    # モデルの取得
    model = get_model(args.model_input)

    # 予測
    pred = score_model(X_test, model)

    # 予測値の保存
    save_data(pred, args.predicted_data)


if __name__ == "__main__":
    # 引数の処理
    args = parse_args()

    # main 関数の実行
    main(args)
