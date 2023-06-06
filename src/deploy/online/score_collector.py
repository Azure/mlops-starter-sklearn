from azureml.ai.monitoring import Collector
import json
import logging
import os
import pandas as pd
import joblib
import numpy


def init():
    """
    This function is called when the container is initialized/started, typically after create/update of the deployment.
    You can write the logic here to perform init operations like caching the model in memory
    """
    global model
    global inputs_collector, outputs_collector
    inputs_collector = Collector(name='model_inputs')          
    outputs_collector = Collector(name='model_outputs')
    # AZUREML_MODEL_DIR is an environment variable created during deployment.
    # It is the path to the model folder (./azureml-models/$MODEL_NAME/$VERSION)
    # Please provide your model's folder name if there is one
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "models/model.pkl")
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)
    logging.info("Init complete")


def run(raw_data):
    """
    This function is called for every invocation of the endpoint to perform the actual scoring/prediction.
    In the example we extract the data from the json input and call the scikit-learn model's predict()
    method and return the result back
    """
    logging.info("model: request received")
    data = json.loads(raw_data)["data"]
    data = numpy.array(data)
    context = inputs_collector.collect(pd.DataFrame(data))
    result = model.predict(data)
    outputs_collector.collect(pd.DataFrame(result), context)
    logging.info("Request processed")
    return result.tolist()
