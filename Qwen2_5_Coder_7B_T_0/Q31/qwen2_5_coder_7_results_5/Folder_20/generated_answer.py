def if_perfect_num(lst):
    return sum([i for i in range(1, lst[53]) if lst[53] % i == 0]) == lst[53]