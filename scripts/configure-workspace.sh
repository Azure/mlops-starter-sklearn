#!/bin/bash

# 環境変数の読み込み
source ./.env

# az ml デフォルトワークスペースの設定
az configure --defaults group=$GROUP workspace=$WORKSPACE location=$LOCATION

az configure -l -o table

echo "Note : リージョン $LOCATION にあるリソースグループ $GROUP の Azure Machine Learning ワークスペース $WORKSPACE をデフォルトのリソースとして設定"
