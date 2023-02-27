import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def reverseString(str):
    start, end = 0, len(str) - 1
    while start < end:
        str[start], str[end] = str[end], str[start]
        start += 1
        end -= 1
    return str


tests = [[["h","e","l","l","o"],["o","l","l","e","h"]],
         [["H","a","n","n","a","h"],["h","a","n","n","a","H"]],
         ]
for i in tests:
    print(assertEquals(reverseString(i[0]),i[1]))
