#!/bin/bash
az ml model create -f ./cli/assets/register_model.yml
az ml model create -f ./cli/assets/register_model_mlflow.yml
