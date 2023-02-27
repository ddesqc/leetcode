import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals

def countOdds(low,high): #not mathematical aproach
    odds = 0
    for i in range(low,high+1):
        if i % 2 == 1:
            odds += 1
    return odds


def countOddsFast(low,high):
    if low % 2 == 0:
        return (high-low+1)//2
    return ((high-low)//2) + 1


tests = [
[3,7,3],
[8,10,1]
]

for i in tests:
    print(assertEquals(countOdds(i[0],i[1]),i[2]))
    print(assertEquals(countOddsFast(i[0],i[1]),i[2]))