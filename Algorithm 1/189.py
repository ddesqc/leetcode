def rotateArray(nums,k):
    start,end = 0, len(nums) - 1
    for i in range(k):
        nums[start], nums[end] = nums[end], nums[start]
        print(nums)
        start += 1
        end -= 1
    return nums
    

def rotateArray2(nums,k):
    k = k % len(nums)
    print(k)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

array = [1,2,3,4,5,6,7]
arr = [-1,-100,3,99]
k = 3
print(rotateArray2(array,k))
print(rotateArray2(arr,2))