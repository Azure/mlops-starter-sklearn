from azureml.core import (
    Dataset,
    Datastore,
    Workspace,
)
from azureml.opendatasets import NycTlcGreen
from datetime import datetime
import pandas as pd
import copy
from dateutil.relativedelta import relativedelta


def register_dataset(ws: Workspace) -> None:
    dataset_name = "nyc_taxi_dataset"
    try:
        dataset = Dataset.get_by_name(
            ws, dataset_name
        )
        df = dataset.to_pandas_dataframe()
    except Exception:
        raw_df = pd.DataFrame([])
        start = datetime.strptime(
            "1/1/2015", "%m/%d/%Y"
        )
        end = datetime.strptime(
            "1/31/2015", "%m/%d/%Y"
        )

        for sample_month in range(3):
            temp_df_green = NycTlcGreen(
                start
                + relativedelta(
                    months=sample_monthっs
                ),
                end
                + relativedelta(
                    months=sample_month
                ),
            ).to_pandas_dataframe()
            raw_df = raw_df.append(
                temp_df_green.sample(2000)
            )

        print(raw_df.head(10))

        df = copy.deepcopy(raw_df)

        columns_to_remove = [
            "lpepDropoffDatetime",
            "puLocationId",
            "doLocationId",
            "extra",
            "mtaTax",
            "improvementSurcharge",
            "tollsAmount",
            "ehailFee",
            "tripType",
            "rateCodeID",
            "storeAndFwdFlag",
            "paymentType",
            "fareAmount",
            "tipAmount",
        ]
        for col in columns_to_remove:
            df.pop(col)

        df = df.query(
            "pickupLatitude>=40.53 and pickupLatitude<=40.88"
        )
        df = df.query(
            "pickupLongitude>=-74.09 and pickupLongitude<=-73.72"
        )
        df = df.query(
            "tripDistance>=0.25 and tripDistance<31"
        )
        df = df.query(
            "passengerCount>0 and totalAmount>0"
        )

        df["lpepPickupDatetime"] = df[
            "lpepPickupDatetime"
        ].map(lambda x: x.timestamp())

        datastore = Datastore.get_default(ws)
        dataset = Dataset.Tabular.register_pandas_dataframe(
            df, datastore, dataset_name
        )

    print(df.head(5))
    df.to_csv(
        "./data/raw/nyx_taxi_dataset.csv",
        header=True,
        index=False,
    )


def main() -> None:
    subscription_id = (
        "9c0f91b8-eb2f-484c-979c-15848c098a6b"
    )
    resource_group = "azureml-mlopshack"
    workspace_name = "azureml-mlopshack"

    ws = Workspace(
        workspace_name=workspace_name,
        subscription_id=subscription_id,
        resource_group=resource_group,
    )

    # Inline Environment によって生成、Environment を使い回す場合以下使用
    # create_environment(ws)
    register_dataset(ws)


if __name__ == "__main__":
    main()
