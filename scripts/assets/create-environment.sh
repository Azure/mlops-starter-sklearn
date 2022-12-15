#!/bin/bash
# Get environment name from yaml file
env_name=$(cat ../../assets/create-environment.yml | grep name | awk '{print $2}')

# Check if environment exists
env_exists=$(az ml environment list --query "[?name=='$env_name']" | jq 'length')

# If environment exists, do not create
if [ $env_exists -gt 0 ]; then
  echo "Environment already exists"
else
  # Create new environment 
  az ml environment create -f ./assets/create-environment.yml
fi
