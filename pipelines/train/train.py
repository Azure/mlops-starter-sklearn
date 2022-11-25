import argparse
from pathlib import Path

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression


def parse_args():
    # 引数の処理
    parser = argparse.ArgumentParser()
    parser.add_argument("--training_data", type=str, help="Path of training_data")
    parser.add_argument("--model_output", type=str, help="Path of training_data")

    args = parser.parse_args()
    return args


def split_label(df):
    X = df.drop(columns="totalAmount")
    y = df["totalAmount"]
    return X, y


def train_model(X_train, y_train):
    # データのサンプル数のロギング
    mlflow.log_metric("Train samples", len(X_train))

    # モデル学習
    model = LinearRegression().fit(X_train, y_train)

    return model


def save_model(model, output_dir):
    # モデルの保存
    mlflow.sklearn.save_model(model, output_dir)


def main(args):
    # 自動ロギングの有効化
    mlflow.autolog(log_models=False)

    # 引数の確認
    lines = [
        f"training_data のパス: {args.training_data}",
        f"モデル出力フォルダのパス: {args.model_output}",
    ]
    [print(line) for line in lines]

    # 学習データの読み込み
    df = pd.read_csv(Path(args.training_data) / "train.csv")

    # データ前処理
    X_train, y_train = split_label(df)

    # モデル学習
    model = train_model(X_train, y_train)

    # モデル保存
    save_model(model, args.model_output)


if __name__ == "__main__":
    # 引数の処理
    args = parse_args()

    # main 関数の実行
    main(args)
