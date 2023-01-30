#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../

az ml model create -f ./cli/assets/register_model.yml
az ml model create -f ./cli/assets/register_model_mlflow.yml
