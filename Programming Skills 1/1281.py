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
def subtractProductAndSum(n):
    nums = [int(x) for x in str(n)]
    return prod(nums) - sum(nums)

tests = [
[234,15],
[4421,21],
[0,0]
]
for i in tests:
    print(assertEquals(subtractProductAndSum(i[0]),i[1]))