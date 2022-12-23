# クイックスタート
本リポジトリを動作させる手順を記載します。

## Azure Machine Learning の環境準備
- Azure の Subscription を準備します。
  ※本リポジトリは所有者権限を持っていることを前提に作成されています。
- [クイックスタート: Azure Machine Learning の利用を開始するために必要なワークスペース リソースを作成する](https://learn.microsoft.com/ja-jp/azure/machine-learning/quickstart-create-resources) の手順に従って、`ワークスペース` と `コンピューティングインスタンス` を作成します。
- [Visual Studio Code で Azure Machine Learning コンピューティング インスタンスに接続する (プレビュー)](https://learn.microsoft.com/ja-jp/azure/machine-learning/how-to-set-up-vs-code-remote?tabs=studio) の手順に従って、`コンピューティングインスタンス` にアクセス可能なことを確認します。


<br />

## GitHub の環境準備
- GitHub のアカウントを準備します。
  ※ Public リポジトリを利用する前提であれば Free (個人向けの基本プラン) で動作しますが、セキュリティ機能などが豊富な Team プランや Enterprise プランの利用を推奨します。
- 本リポジトリを Fork します。
- `コンピューティングインスタンス` のターミナル上で、User フォルダ (Users) 配下の自分の個人フォルダに Fork したリポジトリをクローンします。

```bash
cd User/<username>
git clone https://github.com/<github user/org>/mlops-starter-sklearn
```

<br />

## 環境変数の設定
- `.env.sample` ファイルを `.env` に改名します。
```bash
move .env.sample .env
```
- `.env` ファイルを開いて環境変数を設定します。
   - GROUP: Azure Machine Learning ワークスペースのリソースグループ名
   - WORKSPACE: Azure Machine Learning ワークスペースの名前 
   - LOCATION: Azure Machine Learning ワークスペースのリージョン
   - SUBSCRIPTION: Azure サブスクリプションID

_.env ファイルの記載の例_
```
GROUP="azureml"
WORKSPACE="azureml"
LOCATION="japaneast"
SUBSCRIPTION="xxxxxxxxxxx"
```
## GitHub Actions のシークレット作成
- GitHub Actions のシークレットを作成します。
   - GROUP: Azure Machine Learning ワークスペースのリソースグループ名
   - WORKSPACE: Azure Machine Learning ワークスペースの名前 
   - SUBSCRIPTION: Azure サブスクリプションID
   - AZURE_CREDENTIAL: Azure の接続情報
   ※ Azure Service Principal を利用します。詳細は [GitHub Actions for deploying to Azure](https://github.com/marketplace/actions/azure-login) をご確認ください。
   ※ OpenID Connect の利用も可能ですが、本リポジトリの GitHub Actions は Azure Service Principal を利用することを前提に作成されているため一部修正が必要です。


## シェルスクリプトの実行
- `コンピューティングインスタンス` のターミナル上で、[scripts](../scripts) フォルダの各シェルスクリプトを実行します。
   - Azure CLI ログイン
      - `az login --use-device` コマンドで Azure CLI 認証を行います。
   - [setup.sh](../scripts/setup.sh)
      - conda 仮想環境の作成
      - pre-commit の設定
      - Azure CLI と ML 拡張機能のインストール
   - [configure-workspace.sh](../scripts/configure-workspace.sh)
      - Azure CLI で利用する Azure Machine Learning ワークスペースの設定
   - ノートブック
      - [run-notebooks.sh](../scripts/prototyping/run-notebooks.sh): 実験用ノートブックの実行
   - アセット作成 (計算環境、データ、環境)
      - [create-compute.sh](../scripts/assets/create-compute.sh): コンピューティングクラスターの作成
      - [create-data.sh](../scripts/assets/create-data.sh): Data アセットの作成
      - [create-environment.sh](../scripts/assets/create-environment.sh): 環境の作成
   - ジョブの実行 (モデル学習)
      - [train.sh](../scripts/jobs/train.sh): Azure ML Job 形式でのモデル学習
   - アセットの作成 (モデル登録)
      - [register-model.sh](../scripts/assets/register-model.sh): 学習済みモデルの登録
    - エンドポイントの作成
      - [deploy-online-endpoint-custom.sh](../scripts/endpoints/deploy-online-endpoint-custom.sh): カスタム型モデルのバッチエンドポイントへのデプロイ
      - [deploy-online-endpoint-mlflow.sh](../scripts/endpoints/deploy-online-endpoint-mlflow.sh): MLflow 型モデルのバッチエンドポイントへのデプロイ
      - [deploy-batch-endpoint-custom.sh](../scripts/endpoints/deploy-batch-endpoint-custom.sh): カスタム型モデルのオンラインエンドポイントへのデプロイ
      - [deploy-batch-endpoint-mlflow.sh](../scripts/endpoints/deploy-batch-endpoint-mlflow.sh): MLflow 型モデルのオンラインエンドポイントへのデプロイ

### E2E のスクリプト実行例

```bash
bash ./scripts/setup.sh
az login --use-device
bash ./scripts/configure-workspace.sh

bash ./scripts/prototyping/run-notebooks.sh

bash ./scripts/assets/create-compute.sh
bash ./scripts/assets/create-data.sh
bash ./scripts/assets/create-environment.sh

bash ./scripts/jobs/train.sh

bash ./scripts/assets/register-model.sh
bash ./scripts/assets/register-model.sh

bash ./scripts/endpoints/deploy-online-endpoint-custom.sh
bash ./scripts/endpoints/deploy-online-endpoint-mlflow.sh
bash ./scripts/endpoints/deploy-batch-endpoint-custom.sh
bash ./scripts/endpoints/deploy-batch-endpoint-mlflow.sh
```
    