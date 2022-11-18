# コーディングガイドライン

本リポジトリでコーディングする際のルール、テスト方法やその実装方法を記載します。

---
## 概念
複数のエンジニアによる共同開発において、プロジェクトまたはリポジトリ全体で一貫性を保つことは解釈の違いを減らすことや可読性の向上、引継ぎの工数を減らす観点で重要です。
これらを実現するために、Linterやテキスト解析・整形ツールを使用する方法があります。

---
## ツール
本リポジトリでは、次のツールの活用を推奨します。

- [Linter](#linter)
    - [Flake8](#flake8)
- [Formatter](#formatter)
    - [black](#black)
- [型ヒント](#型ヒント)
    - [mypy](#mypy) 
- [Git hook](#git-hook)
    - [pre-commit](#pre-commit)

### Linter
コンパイラやインタープリタよりも厳しくソースコードをチェックし、文法だけでなく、バグの原因となる記述を検出して警告してくれるツール。例えば、ソースコード内で未使用の変数や初期化されていない変数のチェックします。

#### <u>Flake8</u>
Python コードの静的解析ツールです ([Flake8 の公式ドキュメント](https://flake8.pycqa.org/en/latest/#))。Flake8 は、以下の３つのツールのラッパーであり、単一のスクリプトを起動することですべてのツールを実行します。

- PyFlakes: コードに論理的なエラーが無いかを確認。
- pep8: コードがコーディング規約([PEP8](https://pep8.readthedocs.io/en/latest/))に準じているかを確認
- Ned Batchelder’s McCabe script: 循環的複雑度のチェック。

1. flake8 の Installation
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


### Formatter
ソースコードのスタイル(スペースの数、改行の位置、コメントの書き方など)をチェックし、自動的に修正・整形してくれるツールです。

#### <u>black</u>
black は一貫性、一般性、可読性及びgit差分の削減を追求したFormatterツールです ([black の公式ドキュメント](https://black.readthedocs.io/en/stable/index.html))。blackのコードスタイルは[こちら](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)のドキュメントに示します。
1. blackのInstallation

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
git commit 前に black が自動実行されるようにするためには、Gitで管理しているプロジェクトディレクトリの`.git/hooks/pre-commit`ファイルに下記の記述をすることで可能です。

```sh:pre-commit
#!/bin/bash
black .
```

実行可能なファイルへ権限を付与します。

```sh
chmod +x .git/hooks/pre-commit
```


※ blackを利用していることを示すバッジをREADME.mdに表記する方法

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

▼ こちらを記述。
```md
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
```

### 型ヒント
Python ではオプションで型ヒントがサポートされています。
#### mypy

`mypy` は型ヒントの静的チェックツールです。

```bash
$ mypy train.py
Success: no issues found in 1 source file
```

### Git hook
#### pre-commit
`pre-commit` は Git hook の Python ラッパーです。

<details>
<summary>導入設定の詳細</summary>
<br/>
- パッケージのインストール

```bash
$ pip install pre-commit
```

- サンプルの設定ファイルの生成

```bash
$ pre-commit sample-config > .pre-commit-config.yaml
```

- git hook へのインストール

```bash
$ pre-commit install
```

- 設定 (.pre-commit-config.yaml)

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

- 実行

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
---

## 実装
機械学習ライフサイクルで上記のツールを適用する方法を記載します。

### Prototyping Loop
Prototyping では Data Scientist はインタラクティブにモデルを探索するフェーズです。そのため基本的に Data Scientist の開発環境に上記のツールを導入します。
#### MLflow

#### Visual Studio Code
Visual Studio Code (aka VSCode) は Data Scientist が利用する IDE です。VSCode で Linter (flake8, mypy etc) や Formatter (black etc) が設定できます。

**参考**
- [Editing Python in Visual Studio Code](https://code.visualstudio.com/docs/python/editing)
- [Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)



### Training Loop
#### GitHub Actions, Azure Pipelines
コードが commit もしくは pull request されたことをトリガーにしてコードに対する処理やテスト (Linter, Formatter, Test) を実施したいときに、GitHub Actions や Azure Pipelines を利用してパイプラインを作成します。

**参考**
- [Black with GitHub Actions integration](https://black.readthedocs.io/en/stable/integrations/github_actions.html) : Black の GitHub Actions 実装サンプル
- [pre-commit action](https://github.com/pre-commit/action) : pre-commit の GitHub Actions 実装サンプル


### Operationalizing Loop

---

## 参考情報
- [Code with Engineering](https://microsoft.github.io/code-with-engineering-playbook/)
