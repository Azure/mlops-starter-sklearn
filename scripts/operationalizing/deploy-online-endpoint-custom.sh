#!/bin/bash
az ml online-endpoint create -f ./jobs/online_endpoint.yml

az ml online-deployment create -f ./jobs/online_deployment.yml
