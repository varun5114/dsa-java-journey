import numpy as np

data=np.array([1,2,3,4,5])
print("mean: ",np.mean(data))
print("median: ",np.median(data))
print("min: ",np.min(data))

def predict(x):
    x=x*2
    return x
nums=list(map(int,input().split()))
for n in nums:
    print("Prediction:",predict(n))
