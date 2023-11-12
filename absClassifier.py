###############################################################
# Algo which trains due to gradients with 2 input vectors     #
# after that algo classifies new input vector in absolute way #
###############################################################

import json
import numpy

w = [0,0]

def load_json(name):
    f = open("data_absClassifier.json", "r")
    data = json.load(f)
    if name == "all":
        return data
    return data[name]

def write_json(dict):
    with open("data_absClassifier.json","w") as json_file:
        oldFile = load_json("all")
        z = json.loads(oldFile)
        z.update(dict)
        json.dump(z, "data_absClassifier.json")
def train_neural_network():

    # define network variabel
    training_data = load_json("training_data")
    print(training_data)
    x1 = training_data["x1"]
    x2 = training_data["x2"]
    y = training_data["y"]
    etha = training_data["etha"]
    running_index = training_data["running_index"]

    for r in range(running_index):
        for e in range(len(x1)-1):
            y_predict = x1[e]*w[0]+x2[e]*w[1]
            error = y[e] - y_predict
            w[0] += error*etha*x1[e]
            w[1] += error*etha*x2[e]

train_neural_network()
write_json({"neural_network_configuration": {"w": w}})
print("w1: "+ str(w[0]))
print("w2: "+ str(w[1]))