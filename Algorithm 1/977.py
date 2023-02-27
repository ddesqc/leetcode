def squaresSortedArray(nums):
    start,end = 0, len(nums) - 1
    while start < end:
        nums[start], nums[end] = nums[start]**2, nums[end]**2
        start += 1
        end -= 1
    return sorted(nums)

print(squaresSortedArray([-4,-1,0,3,10]))