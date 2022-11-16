# conda 仮想環境
conda env create -n mlops-train --file ./environments/conda_train.yml
conda init
conda activate mlops-train

# pre-commit
git init .
pre-commit install-hooks

# Azure CLI & ml extension
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash - && az extension add --name ml
