from random import randint

def fact_rec(n, memo = {}):
    if n == 1: return n
    if n not in memo: 
        memo[n] = n * fact_rec(n - 1)
    return memo[n]

def get_all_permutations(n): #trop long après n = 6 time complexity
    memo = []
    fact_number_of_permutation = fact_rec(n)
    while len(memo) != fact_number_of_permutation:
        cur = str(randint(1,n)) + str(randint(1,n)) + str(randint(1,n))
        if cur not in memo:
            memo.append(cur)
    return memo


print(get_all_permutations(5))
