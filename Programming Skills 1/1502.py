import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals

def canMakeArithmeticProgression(arr):
    arr.sort()
    jump = arr[1] - arr[0]
    for i in range(2,len(arr)):
        if jump != arr[i] - arr[i-1]:
            return False
    return True


tests = [
[[3,5,1],True],
[[1,2,4],False],
[[1,3,5,7,9,11,13,15,17],True]
]
for i in tests:
    print(assertEquals(canMakeArithmeticProgression(i[0]),i[1]))
    

#1,3,5,7,9,11,13,15,17