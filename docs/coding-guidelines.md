# コーディングガイドライン

コード品質を改善するために本リポジトリで利用するツールの概要や機械学習システムへの導入方法を記載します。


## 概念

複数のエンジニアによる共同開発において、プロジェクトまたはリポジトリ全体で一貫性を保つことは解釈の違いを減らすことや可読性の向上、引継ぎの工数を減らす観点で重要です。
これらを実現するために、Linter やテキスト解析・整形ツールを使用する方法があります。

本リポジトリでは、次のツールの活用を推奨します。

- [Linter](#linter)
    - [Flake8](#flake8)
- [Formatter](#formatter)
    - [black](#black)
- [型ヒント](#型ヒント)
    - [mypy](#mypy)
- [Git hook](#git-hook)
    - [pre-commit](#pre-commit)

## Install
本テンプレートを利用する際は、まずpre-commit環境、conda環境、Azure CLI v2環境の構築を行います。
 `/.pre-commit-config.yaml` にすでにFlake8、black、isort の設定の記述がされているので次の方法で反映を行います。

※ VSCodeを用いる場合は`.vscode/settings.json` に black、 flake8、isort を設定します。
詳細はこちらの[Editing](https://code.visualstudio.com/docs/python/editing), [Linting](https://code.visualstudio.com/docs/python/linting)のVSCodeのドキュメントをご参考ください。


続いて、pre-commitの内容の反映とconda/Azure CLI環境を設定します。

**devcontainer を利用する場合**</br>
pre-commit のインストールと設定は自動で反映されます。
- [.devcontainer/Dockerfile](.devcontainer/Dockerfile) : devcontainer を構築する Docker ファイル
- [.pre-commit-config.yaml](.pre-commit-config.yaml) : pre-commit の設定

**devcontainer を利用しない場合**</br>
シェルスクリプト [scripts/setup.sh](scripts/setup.sh) を実行してください。

```sh
chmod +x ./scripts/setup.sh #必要に応じて
bash ./scripts/setup.sh
```

その後、git commit 時にpre-commitの動作確認を行ってください。

## CI/CD パイプライン (GitHub Actions)

GitHub にコードがpush された段階で GitHub Actions 上でコードの確認をします。開発端末での漏れを防ぐことができます。

**参考**
- [Black with GitHub Actions integration](https://black.readthedocs.io/en/stable/integrations/github_actions.html) : Black の GitHub Actions 実装サンプル
- [pre-commit action](https://github.com/pre-commit/action) : pre-commit の GitHub Actions 実装サンプル


## 各種ツールの簡易説明
### Linter

コンパイラやインタープリタよりも厳しくソースコードをチェックし、文法だけでなく、バグの原因となる記述を検出して警告してくれるツール。例えば、ソースコード内で未使用の変数や初期化されていない変数のチェックします。

#### <u>◼︎ Flake8</u>
[Flake8](https://flake8.pycqa.org/en/latest/#) は、Python コードの静的解析ツールです。次の３つのツールのラッパーであり、単一のスクリプトを起動することですべてのツールを実行します。

- PyFlakes: コードに論理的なエラーが無いかを確認。
- pep8: コードがコーディング規約([PEP8](https://pep8.readthedocs.io/en/latest/))に準じているかを確認
- Ned Batchelder’s McCabe script: 循環的複雑度のチェック。

<details>
<summary>導入設定の詳細</summary>
<br/>

1. flake8 のインストール
```sh
pip install flake8
```
2. flake8 によるチェックの実行
```sh
flake8 <任意のディレクトリ or Pythonファイル> # チェックしたい対象を指定して実行
```
3. コードの修正箇所の表示 (show-sourceオプションの指定)
```sh
flake8 --show-source <任意のディレクトリ or Pythonファイル> # チェックしたいファイルを指定して実行
```

</details>

<br/>

### Formatter

ソースコードのスタイル(スペースの数、改行の位置、コメントの書き方など)をチェックし、自動的に修正・整形してくれるツールです。

#### <u>◼︎ black</u>
[black](https://black.readthedocs.io/en/stable/index.html) は一貫性、一般性、可読性及び git 差分の削減を追求した Formatter ツールです。black のコードスタイルは[こちら](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)のドキュメントに記載してあります。

<details>
<summary>導入設定の詳細</summary>
<br/>

1. black のインストール

```sh
# 通常
pip install black

# jupyter notebookを対象とする場合
pip install black[jupyter]
```

2. black によるフォーマットの実行

```sh
black <任意のディレクトリ or Pythonファイル> # チェックしたい対象を指定して実行
```
※ git hookの設定 (githookについては本ページの下の方で解説あり)
git commit 前に black が自動実行されるようにするためには、Git で管理しているプロジェクトディレクトリの`.git/hooks/pre-commit`ファイルに下記の記述をすることで可能です。

```sh:pre-commit
#!/bin/bash
black .
```

実行可能なファイルへ権限を付与します。

```sh
chmod +x .git/hooks/pre-commit
```


※ black を利用していることを示すバッジをREADME.mdに表記する方法

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

▼ こちらを記述。
```md
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
```
</details>
<br/>

### 型ヒント

Python ではオプションで型ヒントがサポートされています。

#### <u>◼︎ mypy</u>

[mypy](https://mypy.readthedocs.io/en/stable/index.html#) は型ヒントの静的チェックツールです。Python は関数や変数に対する型を強制しない仕様のため、型に注意して実装する必要があります。mypy は型アノテーションに基づきコードのバグを検知します。

<details>
<summary>導入設定の詳細</summary>
<br/>

1. mypy のインストール
```sh
pip install mypy
```

2. 設定
型情報を保持する stub ファイルが存在しないパッケージに対するエラーを除外するために、次のように _mypy.ini_ に ignore_missing_imports = True を記載します。
```
[mypy-numpy]
ignore_missing_imports = True

[mypy-pandas.*]
ignore_missing_imports = True

[mypy-sklearn.*]
ignore_missing_imports = True

[mypy-matplotlib.*]
ignore_missing_imports = True

[mypy-mlflow.*]
ignore_missing_imports = True

[mypy-azureml.*]
ignore_missing_imports = True

[mypy-dateutil.*]
ignore_missing_imports = True
```

3. mypy による型チェックの実行
```bash
$ mypy train.py
Success: no issues found in 1 source file
```


</details>
<br/>

### Git hook
#### ◼︎ pre-commit
`pre-commit` は Git hook の Python ラッパーです。

<details>
<summary>導入設定の詳細</summary>
<br/>

1. pre-commit のインストール

```bash
$ pip install pre-commit
```

2. サンプルの設定ファイルの生成

```bash
$ pre-commit sample-config > .pre-commit-config.yaml
```

3. git hook へのインストール

```bash
$ pre-commit install
```

4. 設定 (.pre-commit-config.yaml)

```yml
repos:
# サンプルで生成されるもの (pre-commit sample-config > .pre-commit-config.yaml)
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.3.0
    hooks:
    -   id: trailing-whitespace
    - id: no-commit-to-branch
        args: [--branch, main]
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
```

5. pre-commit の 実行

```bash
$ git commit -m "pre-commit demo"
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/vscode/.cache/pre-commit/patch1666333249-14074.
trim trailing whitespace.................................................Passed
don't commit to branch...................................................Passed
fix end of files.........................................................Passed
check yaml...............................................................Passed
check for added large files..............................................Passed
[INFO] Restored changes from /home/vscode/.cache/pre-commit/patch1666333249-14074.
[coding-guideline-v1 c101751] pre-commit demo
 2 files changed, 19 insertions(+), 20 deletions(-)
```
#### 参考

- [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
- [pre-commit](https://pre-commit.com/)

</details>


## インスピレーション
以下の資料が本書に多大なインスピレーションを与えてくれた主な参考資料です。
- [Code with Engineering](https://microsoft.github.io/code-with-engineering-playbook/)
