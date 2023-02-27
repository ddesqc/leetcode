def rotateArray(nums,k):
    start,end = 0, len(nums) - k
    for i in range(k):
        nums[start], nums[end] = nums[-i], nums[start]
        print(nums)
        start += 1
        end -= 1
    return nums
    

array = [1,2,3,4,5,6,7]
k = 3
print(rotateArray(array,k))