<div align="center">
<h1>
<img width="30", src="./docs/images/azureml-icon.svg"> 
&nbsp;
MLOps with Azure Machine Learning
</h1>
Azure Machine Learning + GitHub を利用した MLOps 実装サンプルコード

<a target="_blank" href="https://github.com/Azure/MLInsider-MLOps"><img src="https://img.shields.io/github/stars/Azure/MLInsider-MLOps.svg?style=social&label=Star"></a>

</div>

---

## 概要
本リポジトリは、MLOps のサンプルコードを素早く利用できることを目的に作成されました。Azure Machine Learning と GitHub Actions を利用する想定です。 


## 使い方
- Azure Machine Learning と GitHub の環境を準備します。
- .env ファイルに環境変数の設定をします。
- GitHub の Secrets を作成します。
- [./scripts](./scripts) フォルダの各シェルスクリプトを実行します。
- 更に詳しい手順や参考資料は [./docs/README.md](./docs/README.md) の各ドキュメントを参照してください。


## 技術条件
- GitHub
    - ソースコード管理、CI/CD パイプライン
- Data
    - [NYC タクシー & リムジン協会 - グリーンタクシー運行記録](https://learn.microsoft.com/ja-jp/azure/open-datasets/dataset-taxi-green?tabs=azureml-opendatasets)
- Azure Machine Learning
    - チーム・組織で共有の機械学習プラットフォーム
    - Compute Instance : CPU タイプ、クライアント端末 (もしくは Dev Container に対応した GitHub Codespace など)
    - Compute Cluster : 共有のクラスター環境
- IDE/Editor
    - Visual Studio Code

## コンテンツ
### Assets
**CLI v2 + YAML**
|シナリオ              |YAML ファイル|シェルスクリプト|詳細        |
|--------------------|---------|-----------|-----------|
|Create Data asset   |[assets/create-data.yml](assets/create-data.yml)|[scripts/assets/create-data.sh](scripts/assets/create-data.sh)|データアセットを作成する|
|Create Compute Cluster|[assets/create-compute.yml](assets/create-compute.yml)|[scripts/assets/create-compute.sh](scripts/assets/create-compute.sh)|Compute を作成する|
|Create Environment for training|[assets/create-environment.yml](assets/create-environment.yml)|[scripts/assets/create-environment.sh](scripts/assets/create-environment.sh)|環境を作成する|

### Prototyping
**Notebook**

|シナリオ              |Notebook|シェルスクリプト|詳細        |
|--------------------|---------|-----------|-----------|
|Baseline Notebook   |[notebooks/train-prototyping.ipynb](notebooks/train-prototyping.ipynb)|[scripts/prototyping/run-notebook.sh](scripts/prototyping/run-notebook.sh)|           |


### Training
**CLI v2 + YAML**
|シナリオ              |YAML ファイル|シェルスクリプト|詳細        |
|--------------------|---------|-----------|-----------|
|Job for training model |[jobs/train.yml](jobs/train.yml)           |[scripts/training/train.sh](scripts/training/train.sh)|


**CI/CD Pipeline**
|シナリオ              |YAML ファイル|Status     |詳細        |
|--------------------|---------|-----------|-----------|
|Smoke Test          |[.github/workflows/smoke-testing.yml](.github/workflows/smoke-testing.yml)|[![smoke-testing](https://github.com/Azure/MLInsider-MLOps/actions/workflows/smoke-testing.yml/badge.svg)](https://github.com/Azure/MLInsider-MLOps/actions/workflows/smoke-testing.yml)|           |


### Operationalizing
**CLI v2 + YAML**
|シナリオ                            |YAML ファイル |シェルスクリプト|詳細        |
|----------------------------------|---------|-----------|-----------|
|Create Batch deployment (custom)  |[jobs/batch_deployment.yml](jobs/batch_deployment.yml)|[scripts/operationalizing/deploy-batch-endpoint.sh](scripts/operationalizing/deploy-batch-endpoint-custom.sh)           |           |
|Create Batch deployment (mlflow)  |[jobs/batch_deployment_mlflow.yml](jobs/batch_deployment_mlflow.yml)|[scripts/operationalizing/deploy-batch-endpoint.sh](scripts/operationalizing/deploy-online-endpoint-mlflow.sh)|           |

---
## ディレクトリ構造

>TODO

---

## 免責事項
当社は、外部のリンク先ウェブサイトの内容に関していかなる責任も負うものではありません。お客様は、自らの責任においてこれらのリンクをご利用ください。なお、お客様によるリンクご利用の結果、ないしはリンクご利用に関連して、お客様が被るいかなる損害または損失について当社は、責任を負うものではありません。

## Contributing

We are welcome your contribution from customers and internal microsoft employees. Please see [CONTRIBUTING](./CONTRIBUTING.md).


## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
