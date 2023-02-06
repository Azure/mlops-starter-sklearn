# クイックスタート
## 1. コード実行
サンプルコードを動かす手順を紹介します。

### Azure Machine Learning の環境準備
- Azure の Subscription を準備します。
  - Azure のリソースグループに対する所有者権限を持っていることが前提です。
- [クイックスタート: Azure Machine Learning の利用を開始するために必要なワークスペース リソースを作成する](https://learn.microsoft.com/ja-jp/azure/machine-learning/quickstart-create-resources) の手順に従って、Azure Machine Learning の `ワークスペース` と `コンピューティングインスタンス` を作成します。
- [Visual Studio Code で Azure Machine Learning コンピューティング インスタンスに接続する (プレビュー)](https://learn.microsoft.com/ja-jp/azure/machine-learning/how-to-set-up-vs-code-remote?tabs=studio#configure-a-remote-compute-instance) の手順に従って、Azure Machine Learning の `コンピューティングインスタンス` にアクセス可能なことを確認します。


<br />

### GitHub の環境準備
- GitHub のアカウントを準備します。
  - Public リポジトリを利用する前提であれば Free プラン (個人・組織の基本プラン) の[価格プラン](https://github.com/pricing)で動作しますが、セキュリティ機能などが豊富な Team プランや Enterprise プランの利用を推奨します。
- 本リポジトリ [Azure/mlops-starter-sklearn](https://github.com/Azure/mlops-starter-sklearn) を自分のアカウント・組織に Fork します。
- `コンピューティングインスタンス` のターミナル上で、User フォルダ (Users) 配下の自分の個人フォルダに Fork したリポジトリをクローンします。

```bash
cd User/<username>
git clone https://github.com/<github user/org>/mlops-starter-sklearn #Fork 先のリポジトリを指定
```

<br />

### Azure Machine Learning 上での環境変数の設定
先ほど Fork したコードを実行します。

- `.env.sample` ファイルを `.env` に改名します。
```bash
mv .env.sample .env
```
- `.env` ファイルを開いて環境変数を設定します。
   - GROUP: Azure Machine Learning ワークスペースのリソースグループ名
   - WORKSPACE: Azure Machine Learning ワークスペースの名前
   - LOCATION: Azure Machine Learning ワークスペースのリージョン
      - Azure Clud Shell や (Azure 認証後の) Azure ML の Compute Instance 上 で コマンド `az account list-locations -o table` を実行して Name 列を確認します。DisplayName ではありません。例えば東日本リージョンの場合は Japan East ではなく、japaneast になります。
   - SUBSCRIPTION: Azure サブスクリプションID

_.env ファイルの記載の例_
```
GROUP="azureml"
WORKSPACE="azureml"
LOCATION="japaneast"
SUBSCRIPTION="xxxxxxxxxxx"
```

### シェルスクリプトの実行
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

#### E2E のスクリプト実行例

```bash
# Azure ログイン認証
az login --use-device

# Python 環境の構築、Jupyter カーネルの設定、pre-commit 設定、Azure CLI インストール
bash ./scripts/setup.sh

# 環境変数の読み込みと Azure CLI の設定
bash ./scripts/configure-workspace.sh

# Notebook の実行
bash ./scripts/prototyping/run-notebooks.sh

# アセット (計算環境、データアセット、環境) の作成
bash ./scripts/assets/create-compute.sh
bash ./scripts/assets/create-data.sh
bash ./scripts/assets/create-environment.sh

# Job の実行
bash ./scripts/jobs/train.sh

# モデルの登録
bash ./scripts/assets/register-model.sh

# 推論環境の構築
bash ./scripts/endpoints/deploy-online-endpoint-custom.sh
bash ./scripts/endpoints/deploy-online-endpoint-mlflow.sh
bash ./scripts/endpoints/deploy-batch-endpoint-custom.sh
bash ./scripts/endpoints/deploy-batch-endpoint-mlflow.sh
```

---

## 2. CI/CD の実行

### GitHub Actions のシークレット作成
- GitHub Actions のシークレットを作成します。
   - GROUP: Azure Machine Learning ワークスペースのリソースグループ名
   - WORKSPACE: Azure Machine Learning ワークスペースの名前
   - SUBSCRIPTION: Azure サブスクリプション ID
   - AZURE_CREDENTIALS: Azure の接続情報
      - Azure Service Principal を利用する想定で書かれています。技術的には OpenID Connect の利用も可能ですが、本ドキュメントやコードは Azure Service Principal を利用することを前提に作成されています。
      - 資格情報とそれをシークレット AZURE_CREDENTAL に設定する詳細な方法は [Azure Machine Learning で GitHub Actions を使用する - 手順2. Azure での認証](https://learn.microsoft.com/ja-JP/azure/machine-learning/how-to-github-actions-machine-learning?tabs=userlevel#step-2-authenticate-with-azure) をご参照ください。

### GitHub Actions の有効化と実行
Fork 先の GitHub のページ内の `Actions` タブにアクセスし、GitHub Actions を有効化します。詳細は [GitHub アクション - ワークフローの無効化と有効化](https://docs.github.com/ja/actions/managing-workflow-runs/disabling-and-enabling-a-workflow) をご確認ください。
