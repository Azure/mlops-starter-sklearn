# コーディングガイドライン

本リポジトリでコーディングする際のルール、テスト方法やその実装方法を記載します。

---
## 概念


---
## ツール
次のツールを紹介します。

- [Linter](#linter)
- [Formatter](#formatter)
- [型ヒント](#型ヒント)
- [Git hook](#git-hook)

### Linter
#### flak8

### Formatter
#### black

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

### Training Loop

### Operationalizing Loop

---

## 参考情報
- [Code with Engineering](https://microsoft.github.io/code-with-engineering-playbook/)
