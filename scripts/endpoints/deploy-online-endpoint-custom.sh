#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../

export ENDPOINT_NAME=online-endpoint-custom-`echo $RANDOM`

az ml online-endpoint create --name $ENDPOINT_NAME -f ./cli/endpoints/online_endpoint.yml

az ml online-deployment create --endpoint-name $ENDPOINT_NAME -f ./cli/endpoints/online_deployment.yml
