import argparse
from pathlib import Path

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split


def parse_args():
    # 引数の処理
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data", type=str, help="input data")
    parser.add_argument(
        "--test_split_ratio", type=float, help="Ratio of train test split"
    )
    parser.add_argument("--training_data", type=str, help="Path of training_data")
    parser.add_argument("--testing_data", type=str, help="Path of training_data")

    args = parser.parse_args()
    return args


def process_data(df):
    training_data, testing_data = train_test_split(
        df, test_size=args.test_split_ratio, random_state=0
    )
    mlflow.log_metric("Train samples", len(training_data))
    mlflow.log_metric("Test samples", len(testing_data))

    # 分割データの出力
    return training_data, testing_data


def main(args):
    # 引数の確認
    lines = [
        f"学習データのパス: {args.input_data}",
        f"分割データのパス (training_data): {args.training_data}",
        f"分割データのパス (testing_data): {args.testing_data}",
    ]
    [print(line) for line in lines]

    # 学習データの読み込み
    df = pd.read_csv(args.input_data)

    # データ前処理
    training_data, testing_data = process_data(df)
    training_data.to_csv(Path(args.training_data) / "train.csv", index=False)
    testing_data.to_csv(Path(args.testing_data) / "test.csv", index=False)


if __name__ == "__main__":
    # 引数の処理
    args = parse_args()

    # main 関数の実行
    main(args)
