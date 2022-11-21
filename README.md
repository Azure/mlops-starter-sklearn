<div align="center">
<h1>
<img width="30", src="./docs/images/azureml-icon.svg"> 
&nbsp;
MLOps with Azure Machine Learning
</h1>
Azure Machine Learning + GitHub を利用した MLOps 実装サンプルコード
</div>

## 概要
本リポジトリは MLOps のプラクティスに沿って Azure Machine Learning と GitHub を利用して、モデル学習、デプロイメント、監視をする際のサンプルコードを提供します。

## 前提条件
本リポジトリで利用しているデータ、サービス、ツールを次に挙げます。

### データ
[NYC タクシー & リムジン協会 - グリーンタクシー運行記録](https://learn.microsoft.com/ja-jp/azure/open-datasets/dataset-taxi-green?tabs=azureml-opendatasets)
    - Azure Open Datasets からデータを取得。[utils/prepare_data.py](utils/prepare_data.py) を実行することで入手可能。

### 機械学習プラットフォーム
Azure Machine Learning
- Workspace : 最低 1 つは利用可能なこと
- Compute : Compute Cluster の CPU タイプの計算環境を利用

### クライアント環境
Compute Instance もしくは devcontainer 環境 (GitHub Codespace など)

### その他
#### 統合開発環境 (エディター)
Visual Studio Code
#### コード管理
GitHub
#### パイプライン
GitHub Actions, Azure Machine Learning Pipelines



## セットアップ
- Azure Machine Learning ワークスペースを準備します。
- クライアント環境に必要なソフトウェア (conda 仮想環境、pre-commit、Azure CLI & ml extension) をインストールします。
    - devcontainer を利用する場合
      - 必要なソフトウェアは自動でインストールされます。
    - devcontainer を利用しない場合
      - `scripts/setup.sh` を実行してインストールします。
- `.env.example` を `.env` にファイル名を変更し Azure Machine Learning ワークスペースの情報を記載します。
- 次に、 `scripts/configure-workspace.sh` を実行し、`.env` に記載された環境変数を用いて az コマンドのデフォルトの Azure Machine Learning ワークスペースを設定します。


## 構成
### Assets
**script**
|シナリオ              |パス      |Status     |詳細        |
|--------------------|---------|-----------|-----------|
|Create Data asset   |[assets/create-data.yml](assets/create-data.yml)|           |           |
|Create Compute Cluster|[assets/create-compute.yml](assets/create-compute.yml)|           |           |
|Create Environment for training|[assets/create-environment.yml](assets/create-environment.yml)|           |           |

### Prototyping
**script**

|シナリオ              |パス      |Status     |詳細        |
|--------------------|---------|-----------|-----------|
|Baseline Notebook   |[notebooks/train-prototyping.ipynb](notebooks/train-prototyping.ipynb)|           |           |


### Training
**script**
|シナリオ              |パス      |Status     |詳細        |
|--------------------|---------|-----------|-----------|
|Job for training model |[jobs/train.yml](jobs/train.yml)           |           |
|Smoke Test          |[.github/workflows/smoke-testing.yml](.github/workflows/smoke-testing.yml)|[![smoke-testing](https://github.com/Azure/MLInsider-MLOps/actions/workflows/smoke-testing.yml/badge.svg)](https://github.com/Azure/MLInsider-MLOps/actions/workflows/smoke-testing.yml)|           |


### Operationalizing
**script**
|シナリオ                            |パス      |Status     |詳細        |
|----------------------------------|---------|-----------|-----------|
|Create Batch endpoint             |[jobs/batch_endpoint.yml](jobs/batch_endpoint.yml)|           |           |
|Create Batch deployment (custom)  |[jobs/batch_deployment.yml](jobs/batch_deployment.yml)|           |           |
|Create Batch deployment (mlflow)  |[jobs/batch_deployment_mlflow.yml](jobs/batch_deployment_mlflow.yml)|           |           |

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
