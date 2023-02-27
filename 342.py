# solution 231,342,326 lol 
def is_n_power_of_x(n,x):
    memo = []
    flag = True
    i = 0
    while flag:
        if n in memo:
            flag = False
        else:
            memo.append(x**i)
            i += 1
        if max(memo) > n:
            return False
    return True

print(is_n_power_of_x(16,4))