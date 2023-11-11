x = [1,4,2,0,5,6]
y = [2,8,4,0,10,12]
w = 0
running_index = 100
etha = 0.1
for h in range(running_index):
    for i in range(len(x)-1):
        print("\nIndex: " + str(i))
        print("---------------------")
        print("x: " + str(x[i]))
        print("y: " + str(y[i]))
        print("weight: " + str(w))
        y_predict = x[i]*w
        error = y[i]-y_predict
        w += error*x[i]*etha
        print("y_predict: " + str(y_predict))
        print("error: "+ str(error))
        print("delta_w: "+ str(error*x[i]*etha))