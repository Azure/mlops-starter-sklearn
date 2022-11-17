conda activate mlops-train
cd notebooks
papermill train-prototyping.ipynb out.ipynb -k mlops-train
