#!/bin/bash
export ENDPOINT_NAME=batch-endpoint-custom-`echo $RANDOM`

az ml batch-endpoint create --name $ENDPOINT_NAME -f ./cli/endpoints/batch_endpoint.yml

az ml batch-deployment create --endpoint-name $ENDPOINT_NAME -f ./cli/endpoints/batch_deployment.yml