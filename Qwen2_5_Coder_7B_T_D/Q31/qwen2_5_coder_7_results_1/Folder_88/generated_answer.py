def if_perfect_num(lst):
    return lst[46] == sum([i for i in range(1, lst[46]) if lst[46] % i == 0])