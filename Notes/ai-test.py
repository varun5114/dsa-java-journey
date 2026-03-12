import numpy as np

data=np.array([1,2,3,4,5])
print("mean: ",np.mean(data))
print("median: ",np.median(data))
print("min: ",np.min(data))

def predict(x):
    x=x*2
    return x
while True:
    x=int(input("Enter a number: "))
    print("prediction value: ",predict(x))
