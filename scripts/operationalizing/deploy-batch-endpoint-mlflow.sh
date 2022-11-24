#!/bin/bash
export ENDPOINT_NAME=batch-endpoint-mlflow`echo $RANDOM`

az ml batch-endpoint create --name $ENDPOINT_NAME -f ./jobs/batch_endpoint.yml

az ml batch-deployment create --endpoint-name $ENDPOINT_NAME -f ./jobs/batch_deployment_mlflow.yml
