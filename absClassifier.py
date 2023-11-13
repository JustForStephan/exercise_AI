###############################################################
# Algo which trains due to gradients with 2 input vectors     #
# after that algo classifies new input vector in absolute way #
###############################################################

import json
import numpy

w = [0,0]                                       # list of the weights of the neural network

def load_json(name):                            # loads json data
    f = open("data_absClassifier.json", "r")
    data = json.load(f)
    f.close()
    return data[name]

def estetics_in_json(string):                   # makes the json readable before upload
    string = string.replace("'",'"')
    string = string.replace("],","],\n")
    string = string.replace("{","{\n")
    string = string.replace("}", "\n}")
    string = string.replace(', "',',\n"')
    return string

def write_json(data):                           # updates the json data with the neural_network configuration
    training_data = load_json("training_data")
    to_classify_data = load_json("to_classify")
    new_dict = {"training_data": training_data, "neural_network_configuration": data, "to_classify": to_classify_data}

    json_file = open("data_absClassifier.json", "w")
    json_file.write(estetics_in_json(str(new_dict)))
    json_file.close()

def train_neural_network():                     # def to find adapt the weights due to mathematical greadients

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

def classify_new_data(json_object):
    data = load_json(json_object)
    print(data)

train_neural_network()
print("w1: "+ str(w[0]))
print("w2: "+ str(w[1]))

write_json({"w": w})

classify_new_data("to_classify")