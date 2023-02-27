import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals

def twoSumII(nums,t): # ok but not optimal
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == t:
                return [i+1,j+1]
            
def twoSum(nums,t):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        if nums[lo] + nums[hi] == t:
            return [lo+1,hi+1]
        elif nums[lo] + nums[hi] < t:
            lo += 1
        else:
            hi -= 1

        
print(assertEquals(twoSum([2,7,11,15],9),[1,2]))
print(assertEquals(twoSum([2,3,4],6),[1,3]))
print(assertEquals(twoSum([-1,0],-1),[1,2]))