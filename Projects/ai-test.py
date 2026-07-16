import numpy as np

greater_count = 0
smaller_count = 0
even_count=0
odd_count=0
total_count=0

data = np.array([1,2,3,4,5])

mean_val = np.mean(data)

for i in data:
    total_count+=1
    if mean_val < i:
        greater_count += 1
    elif mean_val > i:
        smaller_count += 1
    if i%2==0:
        even_count+=1
    else: odd_count+=1

nums = []

def cal(n):
    return n*n + 1

__max__=max(nums)
__min__=min(nums)
max_count=0
min_count=0
for n in nums:
    if(n==__max__):
        max_count+=1
    elif(n==__min__):
        min_count+=1


with open("numbers.txt","r") as f:
    for line in f:
        try:
            nums.extend(map(float, line.split()))
        except ValueError:
            print("Invalid number")

print("Process success")
print("Total numbers:", len(nums))

print("\n=========Analysis Report=========")
print("mean:", mean_val)
print("median:", np.median(data))
print("min:", np.min(data))
print("greater_count:", greater_count)
print("smaller_count:", smaller_count)
print("Even count: ",even_count)
print("odd_count: ",odd_count)
for n in nums:
    print("calculated value:", cal(n))

print("Standard Deviation:",np.std(nums))
for n in nums:
    if n > np.median(nums):
        print("Number above median:", n)

print("Max value freq:",max_count)
print("min value freq:",min_count)
nums.sort()
print("sorted numbers:",nums)
nums.sort(reverse=True)
print("desc order numbers:",nums)
print("range:",__max__-__min__)
    