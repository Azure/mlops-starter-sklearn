#!/bin/bash
export ENDPOINT_NAME=online-endpoint-custom-`echo $RANDOM`

az ml online-endpoint create --name $ENDPOINT_NAME -f ./cli/endpoints/online_endpoint.yml

az ml online-deployment create --endpoint-name $ENDPOINT_NAME -f ./cli/endpoints/online_deployment.yml
