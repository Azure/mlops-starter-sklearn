#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../

# 環境変数の読み込み
source .env

# 共同で利用しているサブスクリプションをセット
az account set --subscription $SUBSCRIPTION
# az ml デフォルトワークスペースの設定
az configure --defaults group=$GROUP workspace=$WORKSPACE location=$LOCATION

az configure -l -o table

echo "Note : リージョン $LOCATION にあるリソースグループ $GROUP の Azure Machine Learning ワークスペース $WORKSPACE をデフォルトのリソースとして設定"
