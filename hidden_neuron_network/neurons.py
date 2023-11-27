import random
import numpy

class neuron:

    position = "input_neuron"
    weight = random.random()
    z = 0
    y = 0
    x = []
    w = []
    def __init__(self, x, w):
        self.z = self.calc_z(x,w)
        self.y = self.calc_y(self.z)

    def calc_z(self, x, w):
        print(w)
        z = 0
        for i in range(len(x)):
            z += float(x[i])*float(w[i])
        return z

    def calc_y(self, z):
        return 1/(1+numpy.exp((-1)*z))

    def update(self, x, w):
        self.z = self.calc_z(x, w)
        self.y = self.calc_y(self.z)