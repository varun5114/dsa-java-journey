import numpy as np

greater_count = 0
smaller_count = 0
even_count=0
odd_count=0
total_count=0
unique_numbers=set()
duplicate_numbers=dict()
highest_freq=0

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

with open("numbers.txt","r") as f:
    for line in f:
        try:
            nums.extend(map(float, line.split()))
        except ValueError:
            print("Invalid number")
__max__=max(nums)
__min__=min(nums)
max_count=0
min_count=0
for n in nums:
    if(n==__max__):
        max_count+=1
    elif(n==__min__):
        min_count+=1
for n in nums:
    unique_numbers.add(n)
for n in nums:
    if n in duplicate_numbers:
        duplicate_numbers[n]+=1
    else:
        duplicate_numbers[n]=1

number_above_median=[]
for n in nums:
    if n > np.median(nums):
        number_above_median.append(n)


duplicate_numbers_list=[]
for key,value in duplicate_numbers.items():
    try:
        if value>1:
            duplicate_numbers_list.append(key)
        else:
            raise ValueError
    except ValueError:
        continue
        
    
    if value>highest_freq:
        highest_freq=value
high_freq_numbers=[]
for key,value in duplicate_numbers.items():
    if value==highest_freq:
        high_freq_numbers.extend([key])

count_above_mean=0
for n in nums:
    if n >mean_val:
        count_above_mean+=1

count_below_mean=0
for n in nums:
    if n< mean_val:
        count_below_mean+=1

def generate_report(nums,mean_val,data,greater_count,smaller_count,even_count,odd_count,number_above_median,max_count,min_count,__max__,__min__,unique_numbers,high_freq_numbers,count_above_mean,count_below_mean,duplicate_numbers_list):
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
    print("numbers above median:",number_above_median)
    print("Max value freq:",max_count)
    print("min value freq:",min_count)
    nums.sort()
    print("sorted numbers:",nums)
    nums.sort(reverse=True)
    print("desc order numbers:",nums)
    print("range:",__max__-__min__)
    print("unique numbers are:",unique_numbers)
    print(high_freq_numbers)
    print("largest value",__max__)
    print("smallest value",__min__)
    print("percentage of count above mean:",(count_above_mean/len(nums))*100)
    print("percentage of count_below_mean is:",(count_below_mean/len(nums))*100)
    print("duplicate numbers are:",duplicate_numbers_list if duplicate_numbers_list else "none")

generate_report(
    nums,
    mean_val,
    data,
    greater_count,
    smaller_count,
    even_count,
    odd_count,
    number_above_median,
    max_count,
    min_count,
    __max__,
    __min__,
    unique_numbers,
    high_freq_numbers,
    count_above_mean,
    count_below_mean,
    duplicate_numbers_list
)