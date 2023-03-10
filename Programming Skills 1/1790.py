import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def areAlmostEqual(s1,s2):
    if s1 == s2: return True
    if sorted(s1) != sorted(s2):
        return False
    c = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            c +=1
    if c != 2:
        return False
    return True
        


tests = [
["bank","kanb",True],
["attack","defend",False],
["kelb","kelb",True]
]
for i in tests:
    print(assertEquals(areAlmostEqual(i[0],i[1]),i[2]))