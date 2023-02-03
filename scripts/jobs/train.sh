#!/bin/bash

# move to directory of shell script
exec_path=$(readlink -f "$0")
exec_dir=$(dirname "$exec_path")
cd $exec_dir/../../

az ml job create -f ./cli/jobs/train.yml --stream
