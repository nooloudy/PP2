def has_33(nums):
    for i in range(len(nums) - 1):
        if(nums[i] == nums[i+1] == 3):
            return True
    return False

# print(has_33([1, 3, 3]))