import sys
sys.path.insert(1, '../')
from assertEquals import assertEquals


def reverseWords(s):
    res = ''
    start = end = 0
    while end < len(s):
        if s[end] != ' ':
            end += 1
        elif s[end] == ' ':
            res += s[start:end +1][::-1]
            end += 1
            start = end
    res += ' '
    res += s[start:end + 2][::-1]
    return res[1:]

def reverseWords2(s):
    words = s.split(' ')
    return ' '.join([word[::-1] for word in words])


tests = [
["Let's take LeetCode contest","s'teL ekat edoCteeL tsetnoc"],
["God Ding","doG gniD", "doG gniD"]
]
for i in tests:
    print(assertEquals(reverseWords(i[0]),i[1]))