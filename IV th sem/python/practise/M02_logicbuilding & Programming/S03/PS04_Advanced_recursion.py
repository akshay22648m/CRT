def is_Sortedarray(nums):
    if len(nums) <= 1:
        return True
    if nums[0] > nums[1]:
        return False
    return is_Sortedarray(nums[1:])

print(is_Sortedarray([10,20,30,40,50]))
print(is_Sortedarray(10,2,30,15,50]))
 