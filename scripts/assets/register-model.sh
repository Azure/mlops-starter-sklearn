#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../

# get the latest run id
run_id=$(echo $(az ml job list --query "reverse(sort_by([?status=='Completed'].{experiment_name:experiment_name, run_id:name, status:status, date:creation_context.created_at}, &date))[0].run_id") | sed 's/"//g')
echo $run_id


# register model that was trained in the latest job
az ml model create -f ./cli/assets/register_model.yml --path azureml://datastores/workspaceblobstore/paths/nyc-taxi/$run_id/models
az ml model create -f ./cli/assets/register_model_mlflow.yml --path azureml://datastores/workspaceblobstore/paths/nyc-taxi/$run_id/models
