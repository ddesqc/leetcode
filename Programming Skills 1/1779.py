import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def nearestValidPoint(x,y,points):
    min_dist, ans = float("inf"), -1
    for i, (a, b) in enumerate(points):
        if a == x or b == y:
            man_dist = abs(a - x) + abs(b - y)
            if man_dist < min_dist:
                ans, min_dist = i, man_dist
    return ans


tests = [
[3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]],2],
[3,4,[[3,4]],0],
[3,4,[[2,3]],-1]
]
for i in tests:
    print(assertEquals(nearestValidPoint(i[0],i[1],i[2]),i[3]))