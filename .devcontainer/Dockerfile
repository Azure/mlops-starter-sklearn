# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.238.1/containers/python-3-miniconda/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/miniconda:0-3

COPY ./environments/requirements.txt /environments/
RUN conda create -y --name mlops-train python=3.8 && \
    /bin/bash -c "source activate mlops-train" && \
    pip install -r /environments/requirements.txt

COPY .pre-commit-config.yaml .
RUN git init . && pre-commit install-hooks
