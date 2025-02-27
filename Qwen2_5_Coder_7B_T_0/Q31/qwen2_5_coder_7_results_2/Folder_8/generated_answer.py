def if_perfect_num(lst):
    return sum([i for i in range(1, lst[49]) if lst[49] % i == 0]) == lst[49]