#!/bin/bash
source /anaconda/etc/profile.d/conda.sh
conda activate mlops-train

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../notebooks

papermill train-experiment.ipynb out.ipynb -k mlops-train
papermill train-mlflow-local.ipynb out.ipynb -k mlops-train
papermill train-model-debugging.ipynb out.ipynb -k mlops-train
