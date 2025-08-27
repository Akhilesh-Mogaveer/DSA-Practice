#Two sum 

nums = [2,7,11,15]
target = 9

def two_sum(nums,target):
    value = {}

    for i, num in enumerate(nums):
        if target - num in value:
            return[value[target-num],i]
        value[num] = i
    return []
            
print(two_sum(nums,target))
