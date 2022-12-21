#!/bin/bash
# Get dataset name from yaml file
dataset_name=$(cat ./assets/create-data.yml | grep name | awk '{print $2}')

# Check if dataset exists
dataset_exists=$(az ml data list --query "[?name=='$dataset_name']" | jq 'length')

# If dataset exists, do not create
if [ $dataset_exists -gt 0 ]; then
  echo "Dataset already exists"
else
  # Create new dataset
  az ml data create -f ./assets/create-data.yml
fi
