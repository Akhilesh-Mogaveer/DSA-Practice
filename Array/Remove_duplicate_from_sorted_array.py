#Remove duplicate from sorted array 

nums = [0,0,1,1,1,2,2,3,3,4]


def remove(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            
    return i + 1

print(remove(nums))

