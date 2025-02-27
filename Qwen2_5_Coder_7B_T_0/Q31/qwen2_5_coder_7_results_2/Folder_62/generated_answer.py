def if_perfect_num(lst):
    return sum([i for i in range(1, lst[926]) if lst[926] % i == 0]) == lst[926]