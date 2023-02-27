def moveZeroes(nums): # doesnt conserve non zeroes order
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        i += 1
    return nums

def correctMoveZeroes(nums): #correct way
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums

print(moveZeroes([0,1,0,3,12]))
print(correctMoveZeroes([0,1,0,3,12]))