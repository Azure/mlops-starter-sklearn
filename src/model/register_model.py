import argparse
import os
from pathlib import Path

import mlflow
from mlflow.pyfunc import load_model


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_name",
        type=str,
        help="Name under which model will be registered",
    )
    parser.add_argument(
        "--model_path",
        type=str,
        help="Model directory",
    )
    parser.add_argument(
        "--deploy_flag",
        type=str,
        help="A deploy flag whether to deploy or no",
    )

    args, _ = parser.parse_known_args()
    print(f"Arguments: {args}")

    return args


def main():
    # Get run
    run = mlflow.start_run()
    run_id = run.info.run_id
    print("run_id: ", run_id)

    args = parse_args()

    model_name = args.model_name
    model_path = args.model_path

    if len(args.deploy_flag) == 1:  # this is the case where deploy_flag is a digit
        deploy_flag = int(args.deploy_flag)
    else:  # this is the case where deploy_flag is a path name
        with open(
            (Path(args.deploy_flag) / "deploy_flag"),
            "rb",
        ) as f:
            deploy_flag = int(f.read())

    if deploy_flag == 1:
        print("Registering ", model_name)

        model = load_model(os.path.join(model_path, "models"))
        # log model using mlflow
        mlflow.sklearn.log_model(model, model_name)

        # register model using mlflow model
        model_uri = f"runs:/{run_id}/{args.model_name}"
        mlflow.register_model(model_uri, model_name)

    else:
        print("Model will not be registered!")

    mlflow.end_run()


if __name__ == "__main__":
    main()
