#!/bin/bash
# Get cluster name from yaml file
cluster_name=$(cat ../../assets/create-compute.yml | grep name | awk '{print $2}')

# Check if cluster exists
cluster_exists=$(az ml compute list --query "[?name=='$cluster_name']" | jq 'length')

# If cluster exists, do not create
if [ $cluster_exists -gt 0 ]; then
  echo "Cluster already exists"
else
  # Create new cluster
  az ml compute create -f ./assets/create-compute.yml
fi
