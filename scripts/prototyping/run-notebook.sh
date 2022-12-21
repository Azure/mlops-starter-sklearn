#!/bin/bash
conda activate mlops-train
cd notebooks
papermill train-experiment.ipynb out.ipynb -k mlops-train
papermill train-mlflow-local.ipynb out.ipynb -k mlops-train
papermill train-model-debugging.ipynb out.ipynb -k mlops-train