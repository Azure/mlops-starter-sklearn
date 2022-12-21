#!/bin/bash
export ENDPOINT_NAME=online-endpoint-custom-`echo $RANDOM`

az ml online-endpoint create -f ./endpoints/online_endpoint.yml

az ml online-deployment create -f ./endpoints/online_deployment.yml
