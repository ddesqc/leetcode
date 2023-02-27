def firstBadVersion(n):
    low = 1
    high = n
    while low <= high:
        mid = low + (high - low)//2
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low

def isBadVersion(n):
    if n in [2,5,7]:
        return True
    return False


print(firstBadVersion(9))