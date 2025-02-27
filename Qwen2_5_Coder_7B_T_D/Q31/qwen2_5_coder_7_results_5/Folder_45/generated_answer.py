def if_perfect_num(lst):
    return sum([i for i in range(1, lst[33]) if lst[33] % i == 0]) == lst[33] if len(lst) > 33 else False