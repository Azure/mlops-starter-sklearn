#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../

# Get cluster name from yaml file
cluster_name=$(cat ./cli/assets/create-compute.yml | grep name | awk '{print $2}')

# Check if cluster exists
cluster_exists=$(az ml compute list --query "[?name=='$cluster_name']" | jq 'length')

# If cluster exists, do not create
if [ $cluster_exists -gt 0 ]; then
  echo "Cluster already exists"
else
  # Create new cluster
  az ml compute create -f ./cli/assets/create-compute.yml
fi
