#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../

# conda 仮想環境
# conda環境名を指定
CONDA_ENV_NAME="mlops-train"

# 特定の環境が存在するかどうかを確認
if conda env list | grep -Eq "\s*$CONDA_ENV_NAME\s"; then
    # check if the conda environment already exists
    echo "Conda environment '$CONDA_ENV_NAME' already exists. Skipping creation."
    source /anaconda/etc/profile.d/conda.sh
    conda activate $CONDA_ENV_NAME
else
    # 環境が存在しない場合はエラーメッセージを表示
    conda env create -n $CONDA_ENV_NAME --file environments/conda_train.yml

    conda init bash
    # check if the command was successful
    if [ $? -eq 0 ]; then
        echo "'conda init' command was successful."
    fi

    source /anaconda/etc/profile.d/conda.sh
    conda activate $CONDA_ENV_NAME

    # check if the command was successful
    if [ $? -eq 0 ]; then
        echo "'conda activate $CONDA_ENV_NAME' command was successful."
    fi
fi


# ipykernel
ipython kernel install --user --name=$CONDA_ENV_NAME --display-name=$CONDA_ENV_NAME

# pre-commit
git init .
git config --global --add safe.directory .
pre-commit install-hooks

# Azure CLI & ml extension
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash - && az extension add --name ml
