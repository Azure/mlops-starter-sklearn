#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../

# Get dataset name from yaml file
dataset_name=$(cat ./cli/assets/create-data.yml | grep name | awk '{print $2}')

# Check if dataset exists
dataset_exists=$(az ml data list --query "[?name=='$dataset_name']" | jq 'length')

# If dataset exists, do not create
if [ $dataset_exists -gt 0 ]; then
  echo "Dataset already exists"
else
  # Create new dataset
  az ml data create -f ./cli/assets/create-data.yml
fi
