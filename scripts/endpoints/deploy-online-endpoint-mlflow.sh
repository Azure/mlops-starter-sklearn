#!/bin/bash
export ENDPOINT_NAME=online-endpoint-mlflow-`echo $RANDOM`

az ml online-endpoint create --name $ENDPOINT_NAME -f ./endpoints/online_endpoint.yml

az ml online-deployment create --endpoint-name $ENDPOINT_NAME -f ./endpoints/online_deployment_mlflow.yml
