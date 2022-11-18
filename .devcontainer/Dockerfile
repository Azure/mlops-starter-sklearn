FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3
SHELL ["/bin/bash", "-c"]

# conda インストール
COPY ./environments/conda_train.yml /environments/
RUN conda env create -n mlops-train --file /environments/conda_train.yml  && \
    conda init bash

# kernel の設定
RUN source ~/.bashrc && conda activate mlops-train && \
    ipython kernel install --name=mlops-train --display-name=mlops-train

# pre-commit 設定
COPY .pre-commit-config.yaml .
RUN source ~/.bashrc && conda activate mlops-train && \
    git init . && \
    pre-commit install-hooks

# vscode ユーザへ切り替え
USER vscode

# Azure CLI & ml extension のインストール
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash - && az extension add --name ml

# conda の設定
RUN conda init bash
