def if_perfect_num(lst):
    return sum([i for i in range(1, lst[60]) if lst[60] % i == 0]) == lst[60]