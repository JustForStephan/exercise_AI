###############################################################
# Algo which trains due to gradients with 2 input vectors     #
# after that algo classifies new input vector in absolute way #
###############################################################

import json
import numpy

w = [0,0]                                       # list of the weights of the neural network
y = []                                          # list of all classified data from json

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

def write_json(data, index):                           # updates the json data with the neural_network configuration

    training_data = load_json("training_data")
    to_classify_data = load_json("to_classify")

    if index == 0:
        new_dict = {"training_data": training_data, "neural_network_configuration": data, "to_classify": to_classify_data}
        json_file = open("data_absClassifier.json", "w")
        json_file.write(estetics_in_json(str(new_dict)))
        json_file.close()

    if index == 1:
        neural_network_config = load_json("neural_network_configuration")
        x1 = to_classify_data["x1"]
        x2 = to_classify_data["x2"]
        new_to_classify = {"x1": x1,"x2":x2,"y":data}
        dict = {"training_data": training_data, "neural_network_configuration": neural_network_config, "to_classify": new_to_classify}
        string_dict = estetics_in_json(str(dict))
        json_file = open("data_absClassifier.json","w")
        json_file.write(string_dict)
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
    x1 = data["x1"]
    x2 = data["x2"]
    for i in range(len(x1)-1):
        y.append(x1[i]*w[0]+x2[i]*w[1])

train_neural_network()
print("Weights got adapted: ")
print("w1: "+ str(w[0]))
print("w2: "+ str(w[1]))
write_json({"w": w},0)
print("\nWeights got safed in: data_absClassifier.json")
classify_new_data("to_classify")
print("\nnew data got classified:")
print("y: ", str(y))
write_json(y,1)
print("\nnew classified values got safed in: data_abs_Classifier.json")
print("--------------------")
print("Algorithm terminated")
