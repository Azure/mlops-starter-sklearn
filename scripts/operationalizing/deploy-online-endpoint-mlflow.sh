#!/bin/bash
export ENDPOINT_NAME=endpt-mlops-`echo $RANDOM`
az ml online-endpoint create --name $ENDPOINT_NAME -f ./jobs/online_endpoint.yml

az ml online-deployment create -f ./jobs/online_deployment_mlflow.yml
