def power_value_of_x(x):
    power_values = []
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        elif x % 2 == 1:
            x = 3 * x + 1
        power_values.append(int(x))
    return len(power_values)

def return_the_k_integer_in_range_lo_hi(lo,hi,k):
    memo = {}
    for i in range(lo,hi+1):
        memo[i] = power_value_of_x(i)
    d = sorted(memo.items(), key=lambda x: x[1])
    return d

print(return_the_k_integer_in_range_lo_hi(12,15,4))
print(power_value_of_x(12)) 