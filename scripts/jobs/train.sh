#!/bin/bash
az ml job create -f ./cli/jobs/train.yml --stream
