def searchInsert(array,target):
    low = 0
    high = len(array) - 1
    nearest = 0
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
            nearest = low
        else:
            high = mid - 1
            nearest = high + 1
    return nearest