az ml batch-endpoint create -f ./jobs/batch_endpoint.yml

az ml batch-deployment create -f ./jobs/batch_deployment_mlflow.yml
