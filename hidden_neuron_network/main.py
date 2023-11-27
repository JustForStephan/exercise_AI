from neurons import neuron

w = [[float(1),float(1)], [float(1), float(1)], [float(1), float(1)], [float(1)], [float(1)]]

etha = 1
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for a in range(len(x)):
    x[a] = float(x[a])
    y[a] = float(y[a])

#declaration of neurons
neuron1 = neuron([1], [w[1][0]])
neuron2 = neuron([1], [w[1][1]])
neuron3 = neuron([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
neuron4 = neuron([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
neuron5 = neuron([neuron3.y, neuron4.y], [w[3], w[4]])

# loop for training index
for running_index in range(100):
    # loop for length of input
    for i in range(len(x)):
        neuron1.update([x[i]], [w[1][0]])
        neuron2.update([1], [w[1][1]])
        neuron3.update([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
        neuron4.update([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
        neuron5.update([neuron3.y, neuron4.y], [w[3], w[4]])
        e = y[i] - neuron5.y

        w[3] += 2 * e * neuron5.z * (1 - neuron5.z) * neuron3.y * etha
        w[4] += 2 * e * neuron5.z * (1 - neuron5.z) * neuron4.y * etha
        w[1][0] += 2 * e * neuron5.z * (1 - neuron5.z) * w[3] * neuron3.z * (1 - neuron3.z) * neuron1.y * etha
        w[1][1] += 2 * e * neuron5.z * (1 - neuron5.z) * w[4] * neuron4.z * (1 - neuron4.z) * neuron1.y * etha
        w[2][0] += 2 * e * neuron5.z * (1 - neuron5.z) * w[3] * neuron3.z * (1 - neuron3.z) * neuron2.y * etha
        w[2][1] += 2 * e * neuron5.z * (1 - neuron5.z) * w[4] * neuron4.z * (1 - neuron4.z) * neuron2.y * etha




new_y = []
for i in range(len(x)):
    neuron1 = neuron(x[i], [w[0][0]])
    neuron2 = neuron([1], w[0][1])
    neuron3 = neuron([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
    neuron4 = neuron([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
    neuron5 = neuron([neuron3.y, neuron4.y], [w[3], w[4]])
    new_y.append(neuron5.y)

print("--------------------------------\n\n\n")
print(x)
print(new_y)

x = 10
n1 = neuron(x, [w[0][0]])
n2 = neuron([1], w[0][1])
n3 = neuron([n1.y, n2.y], [w[1][0], w[2][0]])
n4 = neuron([n1.y, n2.y], [w[1][1], w[2][1]])
n5 = neuron([n3.y, n4.y], [w[3], w[4]])

print(n5.y)