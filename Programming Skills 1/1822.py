import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def prod(lst):
    if not lst:
        return 0
    r = 1
    for x in lst:
        r *= x
    return r


def arraySign(nums):
    p = prod(nums)
    if p > 0:
        return 1
    elif p < 0:
        return -1
    return 0


tests = [
[[-1,-2,-3,-4,3,2,1],1],
[[1,5,0,2,-3],0],
[[-1,1,-1,1,-1],-1]
]
for i in tests:
    print(assertEquals(arraySign(i[0]),i[1]))