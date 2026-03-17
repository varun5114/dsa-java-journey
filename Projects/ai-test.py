import numpy as np


data=np.array([1,2,3,4,5])
print("mean: ",np.mean(data))
print("median: ",np.median(data))
print("min: ",np.min(data))

def predict(x):
    x=x*2
    return x

with open("numbers.txt","r") as files:
    data=files.read()
    nums=list(map(float,data.split()))
    print (nums)
    for n in nums:
        print(f"predicted {n} for:",predict(n))