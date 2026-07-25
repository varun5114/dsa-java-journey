import numpy as np

unique_numbers=set()
duplicate_numbers=dict()
max_count=0
min_count=0

data = np.array([1,2,3,4,5])

def read_file():
    numbers=[]
    with open("numbers.txt","r") as f:
        for line in f:
            try:
                numbers.extend(map(float, line.split()))
            except ValueError:
                print("Invalid number")
    return numbers

nums = read_file()
mean_val = np.mean(nums)

for n in nums:
    unique_numbers.add(n)

def find_duplicates(nums):
    highest_freq=0
    for n in nums:
        if n in duplicate_numbers:
            duplicate_numbers[n]+=1
        else:
            duplicate_numbers[n]=1
    duplicate_numbers_list=[]
    for key,value in duplicate_numbers.items():
        if value>1:
            duplicate_numbers_list.append(key)
        if value > highest_freq:
                highest_freq=value
    return duplicate_numbers_list,highest_freq

duplicate_numbers_list,highest_freq=find_duplicates(nums)

def find_max_min(nums):
    max_val=max(nums)
    min_val=min(nums)
    return max_val,min_val

__max__,__min__=find_max_min(nums)

for n in nums:
    if(n==__max__):
        max_count+=1
    elif(n==__min__):
        min_count+=1

def find_odd_even(nums):
    greater_count = 0
    smaller_count = 0
    even_count=0
    odd_count=0
    total_count=0
    for i in nums:
        total_count+=1
        if mean_val < i:
            greater_count += 1
        elif mean_val > i:
            smaller_count += 1
        if i%2==0:
            even_count+=1
        else: odd_count+=1
    return even_count,odd_count,total_count,greater_count,smaller_count

even_count,odd_count,total_count,greater_count,smaller_count=find_odd_even(nums)


def calculate_statistics(nums):
    number_above_median=[]
    for n in nums:
        if n > np.median(nums):
            number_above_median.append(n)

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
    return number_above_median,high_freq_numbers,count_above_mean,count_below_mean


number_above_median,high_freq_numbers,count_above_mean,count_below_mean=calculate_statistics(nums)

def cal(n):
    return n*n + 1


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
    print(sorted(nums))
    print(sorted(nums,reverse=True))
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