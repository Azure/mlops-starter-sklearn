#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../

# Get environment name from yaml file
env_name=$(cat ./cli/assets/create-environment.yml | grep name | awk '{print $2}')

# Check if environment exists
env_exists=$(az ml environment list --query "[?name=='$env_name']" | jq 'length')

# If environment exists, do not create
if [ $env_exists -gt 0 ]; then
  echo "Environment already exists"
else
  # Create new environment
  az ml environment create -f ./cli/assets/create-environment.yml
fi
