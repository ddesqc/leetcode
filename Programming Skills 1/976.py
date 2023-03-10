import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def largestPerimeter(nums):
    nums = sorted(nums, reverse=True) # same as sorted(A)[::-1]
    for i in range(2,len(nums)):
        if nums[i-2] < nums[i-1] + nums[i]:
            return nums[i-2] + nums[i-1] + nums[i]
    return 0

tests = [
[[2,1,2],5],
[[1,2,1,10],0]
]
for i in tests:
    print(assertEquals(largestPerimeter(i[0]),i[1]))