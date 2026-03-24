import numpy as np
greater_count=0
smaller_count=0

data=np.array([1,2,3,4,5])
print("mean: ",np.mean(data))
for i in data:
    if(np.mean(data)<i):
        greater_count+=1
    elif(np.mean(data)>i):
        smaller_count+=1
print("median: ",np.median(data))
print("min: ",np.min(data))
print("Greater_count: ",greater_count)
print("smaller_count:",smaller_count)

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

