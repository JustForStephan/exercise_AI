# define all values
x1 = [1,3,5,0,2,1,8,10]
x2 = [0.5,1,6,0,5,2,9,3]
y = [2,5,17,0,12,5,26,16]
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


