def if_perfect_num(lst):
    return sum([i for i in range(1, lst[23]) if lst[23] % i == 0]) == lst[23] if len(lst) > 23 else False