# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.238.1/containers/python-3-miniconda/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3
SHELL ["/bin/bash", "-c", "-l"]
COPY ./environments/conda_train.yml /environments/

RUN conda env create -n mlops-train --file /environments/conda_train.yml  && \
    conda init

COPY .pre-commit-config.yaml .

RUN conda activate mlops-train && \
    ipython kernel install --user --name=mlops-train --display-name=mlops-train && \
    git init . && \
    pre-commit install-hooks
