# create environment

```
conda env create --prefix ./.env --file environment.yml
```

If you place this repository on WSL2 /mnt/* or AzureML Compute Instance working directory, we recommend to change ```--prefix ./.env``` to ```--prefix ~/azureml-mlops-env``` because of storage latency.


# update environment

1. Add new package name and version to environment.yml.
1. ```conda env update --prefix ./.env --file environment.yml```