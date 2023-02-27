def binarySearch(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = low +(high - low)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [-1,0,3,5,9,12]
target = 9
res = binarySearch(nums,target)
print(res)
