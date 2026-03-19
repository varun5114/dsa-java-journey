import numpy as np


data=np.array([1,2,3,4,5])
print("mean: ",np.mean(data))
print("median: ",np.median(data))
print("min: ",np.min(data))

def predict(x):
    x=x*2
    return x
nums=[]
with open("numbers.txt","r") as files:
    for line in files:
        nums.extend(map(float,line.split()))
print(nums)
count=0
for n in nums:
    count+=1
    print(f"predicted value: {predict(n)}")

