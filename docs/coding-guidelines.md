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


---

## 実装
機械学習ライフサイクルで上記のツールを適用する方法を記載します。

### Prototyping Loop

### Training Loop

### Operationalizing Loop

---

## 参考情報
- [Code with Engineering](https://microsoft.github.io/code-with-engineering-playbook/)
