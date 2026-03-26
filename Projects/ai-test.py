import numpy as np

greater_count = 0
smaller_count = 0

data = np.array([1,2,3,4,5])

mean_val = np.mean(data)

print("mean:", mean_val)
print("median:", np.median(data))
print("min:", np.min(data))

for i in data:
    if mean_val < i:
        greater_count += 1
    elif mean_val > i:
        smaller_count += 1

print("greater_count:", greater_count)
print("smaller_count:", smaller_count)


nums = []

def cal(n):
    return n*n + 1


with open("numbers.txt","r") as f:
    for line in f:
        try:
            nums.extend(map(float, line.split()))
        except ValueError:
            print("Invalid number")

print("Process success")

print("Total numbers:", len(nums))

for n in nums:
    print("calculated value:", cal(n))