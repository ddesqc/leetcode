import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def hammingWeightWeird(n): #weird
    binStr = str(bin(n))
    return binStr.count('1')


def hammingWeight(n): #gg wp
    ans = 0
    while n:
        n &= (n-1) #
        ans += 1
    return ans

tests = [
[0b00000000000000000000000000001011,3],
[0b00000000000000000000000010000000,1],
[0b11111111111111111111111111111101,31]
]
for i in tests:
    print(assertEquals(hammingWeight(i[0]),i[1]))