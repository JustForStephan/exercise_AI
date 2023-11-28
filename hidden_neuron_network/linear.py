# define all values
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x2 = [1,1,1,1,1,1,1,1,1,1]
y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
w = [0,0]
etha = 0.01
running_index = 10000

# training loop
for i in range(running_index):
    # going through the vectors and calculate the gradients for the weights
    for h in range(len(x1)-1):
        print("running_index "+ str(i))
        print("--------------")
        y_predict = x1[h]*w[0]+x2[h]*w[1]
        error = y[h]-y_predict   # error-func = e²
        w[0] += error*x1[h]*etha # derivation of the error-func for the weight w[0]
        w[1] += error*x2[h]*etha # derivation of the error-func for the weight w[1]
        print("w1:" +str(w[0]))
        print("w2: "+str(w[1]))


new_y = []
for i in range(len(x1)):
    new_y.append(x1[i]*w[0]+x2[i]*w[1])
for f in range(len(x1)):
    print(x1[f])
    print(new_y[f])
