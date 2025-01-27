def min(nums: list[int]) -> str:
    min = float("inf")
    for num in nums:
        if num<min :
            min = num
    
    return print("Min : ", min)

def max(nums: list[int]) -> str:
    max = float("-inf")
    for num in nums:
        if num>max:
            max = num
    return print("Max : ", max)

def avg(nums: list[int]) -> str:
    sum = 0
    for num in nums:
        sum+=num
    
    return print("Avg : ", sum/len(nums))


print("Enter five numbers")

nums = []

for i in range(5):
    try:
        nums.append(int(input("Enter num : ")))
    except:
        print("Enter only integer values")
min(nums)
max(nums)
avg(nums)
