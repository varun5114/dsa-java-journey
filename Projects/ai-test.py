import numpy as np


data=np.array([1,2,3,4,5])
print("mean: ",np.mean(data))
print("median: ",np.median(data))
print("min: ",np.min(data))

count=0
nums=[]
def cal(n):
    return n*n 

with open("numbers.txt","r")as f:
    for line in f:
        nums.extend(map(float,line.split()))

for n in nums:
    count+=1
    print("calculated value: ",cal(n))

