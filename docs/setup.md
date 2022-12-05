## セットアップ
- Azure Machine Learning ワークスペースを準備します。
- クライアント環境に必要なソフトウェア (conda 仮想環境、pre-commit、Azure CLI & ml extension) をインストールします。
    - devcontainer を利用する場合
      - 必要なソフトウェアは自動でインストールされます。
    - devcontainer を利用しない場合
      - `scripts/setup.sh` を実行してインストールします。
- `.env.example` を `.env` にファイル名を変更し Azure Machine Learning ワークスペースの情報を記載します。
- 次に、 `scripts/configure-workspace.sh` を実行し、`.env` に記載された環境変数を用いて az コマンドのデフォルトの Azure Machine Learning ワークスペースを設定します。