import numpy as np

def read_file():
    numbers=[]
    with open("numbers.txt","r") as f:
        for line in f:
            try:
                numbers.extend(map(float, line.split()))
            except ValueError:
                print("Invalid number")
    return numbers

def find_duplicates(nums):
    duplicate_numbers=dict()
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
    return duplicate_numbers_list,highest_freq,duplicate_numbers

def find_max_min(nums):
    max_val=max(nums)
    min_val=min(nums)
    return max_val,min_val

def find_odd_even(nums,mean_val):
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

def calculate_statistics(nums,duplicate_numbers,highest_freq,mean_val):
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

def cal(n):
    return n*n + 1

def generate_report(nums,total_count,mean_val,greater_count,smaller_count,even_count,odd_count,number_above_median,max_count,min_count,__max__,__min__,unique_numbers,high_freq_numbers,count_above_mean,count_below_mean,duplicate_numbers_list):
    print("Process success")
    print("Total numbers:", len(nums))
    print("\n=========Analysis Report=========")
    print("mean:", mean_val)
    print("median:", np.median(nums))
    print("min:", np.min(nums))
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
    print("total count:",total_count)
    print("largest value",__max__)
    print("smallest value",__min__)
    print("percentage of count above mean:",(count_above_mean/len(nums))*100)
    print("percentage of count_below_mean is:",(count_below_mean/len(nums))*100)
    print("duplicate numbers are:",duplicate_numbers_list if duplicate_numbers_list else "none")

def save_report(nums,total_count,mean_val,greater_count,smaller_count,even_count,odd_count,number_above_median,max_count,min_count,__max__,__min__,unique_numbers,high_freq_numbers,count_above_mean,count_below_mean,duplicate_numbers_list):
    with open("report.txt","w") as f:
        f.write("Process success\n")
        f.write("Total numbers: "+str(len(nums))+"\n")
        f.write("\n=========Analysis Report=========\n")
        f.write("mean: "+str(mean_val)+"\n")
        f.write("median: "+str(np.median(nums))+"\n")
        f.write("min: "+str(np.min(nums))+"\n")
        f.write("greater_count: "+str(greater_count)+"\n")
        f.write("smaller_count: "+str(smaller_count)+"\n")
        f.write("Even count: "+str(even_count)+"\n")
        f.write("odd_count: "+str(odd_count)+"\n")
        for n in nums:
            f.write("calculated value: "+str(cal(n))+"\n")

        f.write("Standard Deviation: "+str(np.std(nums))+"\n")
        f.write("numbers above median: "+str(number_above_median)+"\n")
        f.write("Max value freq: "+str(max_count)+"\n")
        f.write("min value freq: "+str(min_count)+"\n")
        f.write(str(sorted(nums))+"\n")
        f.write(str(sorted(nums,reverse=True))+"\n")
        f.write("range: "+str(__max__-__min__)+"\n")
        f.write("unique numbers are: "+str(unique_numbers)+"\n")
        f.write(str(high_freq_numbers)+"\n")
        f.write("total count: "+str(total_count)+"\n")
        f.write("largest value"+str(__max__)+"\n")
        f.write("smallest value"+str(__min__)+"\n")
        f.write("percentage of count above mean:"+ str((count_above_mean/len(nums))*100)+"\n")
        f.write("percentage of count_below_mean is:"+ str((count_below_mean/len(nums))*100)+"\n")
        f.write("duplicate numbers are:"+ str(duplicate_numbers_list if duplicate_numbers_list else "none")+"\n")

def main():    

    unique_numbers=set()
    max_count=0
    min_count=0

    data = np.array([1,2,3,4,5])
    nums = read_file()
    mean_val = np.mean(nums)
    
    for n in nums:
        unique_numbers.add(n)

    __max__,__min__=find_max_min(nums)
    for n in nums:
        if(n==__max__):
            max_count+=1
        elif(n==__min__):
            min_count+=1
    duplicate_numbers_list,highest_freq,duplicate_numbers=find_duplicates(nums)
    even_count,odd_count,total_count,greater_count,smaller_count=find_odd_even(nums,mean_val)
    number_above_median,high_freq_numbers,count_above_mean,count_below_mean=calculate_statistics(nums,duplicate_numbers,highest_freq,mean_val)
    generate_report(nums,total_count,mean_val,data,greater_count,smaller_count,even_count,odd_count,number_above_median,max_count,min_count,__max__,__min__,unique_numbers,high_freq_numbers,count_above_mean,count_below_mean,duplicate_numbers_list)
    save_report(nums,total_count,mean_val,data,greater_count,smaller_count,even_count,odd_count,number_above_median,max_count,min_count,__max__,__min__,unique_numbers,high_freq_numbers,count_above_mean,count_below_mean,duplicate_numbers_list)
if __name__=='__main__':
    main()