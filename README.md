# MLOps with Azure Machine Learning
## 概要
本リポジトリは MLOps のプラクティスに沿って Azure Machine Learning と GitHub を利用して、モデル学習、デプロイメント、監視をする際のサンプルコードを提供します。

## 前提条件
- データ: [NYC タクシー & リムジン協会 - グリーンタクシー運行記録](https://learn.microsoft.com/ja-jp/azure/open-datasets/dataset-taxi-green?tabs=azureml-opendatasets)
- 機械学習プラットフォーム : Azure Machine Learning
    - Workspace : 最低 1 つは利用可能なこと
    - Compute : Compute Instance、Compute Cluster の CPU タイプの計算環境を利用
- コード管理 : GitHub
- パイプライン : Azure Machine Learning Pipeline、GitHub Actions
- IDE (Editor) : Visual Studio Code (Compute Instance に Remote 接続)
---

## 構成
### Assets
**script**
|シナリオ              |パス      |Status     |詳細        |
|--------------------|---------|-----------|-----------|
|Data                |[assets/create-data.yml](assets/create-data.yml)|           |           |
|Compute             |[assets/create-compute.yml](assets/create-compute.yml)|           |           |
|Environment         |[assets/create-environment.yml](assets/create-environment.yml)|           |           |

### Prototyping
**script**

|シナリオ              |パス      |Status     |詳細        |
|--------------------|---------|-----------|-----------|
|Baseline Notebook   |[notebooks/train-prototyping.ipynb](notebooks/train-prototyping.ipynb)|           |           |
|Notebook with MLflow|         |           |           |


### Training
**script**
|シナリオ              |パス      |Status     |詳細        |
|--------------------|---------|-----------|-----------|
|Job                 |[jobs/train.yml](jobs/train.yml)           |           |
|HyperParamter Tune  |         |           |           |
|Smoke Test          |[.github/workflows/smoke-testing.yml](.github/workflows/smoke-testing.yml)|[![smoke-testing](https://github.com/Azure/MLInsider-MLOps/actions/workflows/smoke-testing.yml/badge.svg)](https://github.com/Azure/MLInsider-MLOps/actions/workflows/smoke-testing.yml)|           |


### Operationalizing
**script**
|シナリオ                            |パス      |Status     |詳細        |
|----------------------------------|---------|-----------|-----------|
|Deploy to Managed Online Endpoint |         |           |           |
|Deploy to Batch Endpoint          |         |           |           |

---
## ディレクトリ構造


---

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft 
trademarks or logos is subject to and must follow 
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
