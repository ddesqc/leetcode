def is_power_of_two(n):
    memo = []
    flag = True
    i = 0
    while flag:
        if n in memo:
            flag = False
        else:
            memo.append(2**i)
            i += 1
        if max(memo) > n:
            return False
    return True

print(is_power_of_two(3))