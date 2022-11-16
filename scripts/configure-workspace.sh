source ./.env

az configure --defaults group=$GROUP workspace=$WORKSPACE location=$LOCATION

az configure -l -o table

echo "Note : リージョン $LOCATION にあるリソースグループ $GROUP の Azure Machine Learning ワークスペース $WORKSPACE をデフォルトのリソースとして設定"
