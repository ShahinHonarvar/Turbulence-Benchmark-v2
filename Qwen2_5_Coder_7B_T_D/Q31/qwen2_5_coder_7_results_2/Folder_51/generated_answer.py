def if_perfect_num(lst):
    return lst[64] == sum([i for i in range(1, lst[64]) if lst[64] % i == 0])