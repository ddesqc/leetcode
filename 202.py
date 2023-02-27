n = 19


def sum_of_square(n):
    n_list = [int(x)**2 for x in str(n)]
    return sum(n_list)

def happy_number(n):
    memo = []
    flag = True
    i = sum([int(x)**2 for x in str(n)])
    while flag:
        if i == 1:
            flag = False
        if i not in memo:
            memo.append(i)
            i = sum([int(x)**2 for x in str(i)])
        else:
            return False
    return True


def happy_number_t(i):
    memo = []
    while i != 1:
        if i == 1:
            break
        if i not in memo:
            memo.append(i)
            i = sum([int(x)**2 for x in str(i)])
        else:
            return False
    return True


def affichage_happy_number(n):
    for i in range(1,n+1):
        print(f"{i} : {happy_number(i)}")


affichage_happy_number(100)