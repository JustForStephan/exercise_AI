###############################################################
# Algo which trains due to gradients with 2 input vectors     #
# after that algo classifies new input vector in absolute way #
###############################################################

import json
import numpy

def load_json(permission, name):
    f = open("data_absClassifier.json",permission)
    data = json.load(f)
    return data[name]

training_data = load_json("r", "training_data")
print(training_data)