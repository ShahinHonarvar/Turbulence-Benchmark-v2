def if_perfect_num(lst):
    return sum([i for i in range(1, lst[27]) if lst[27] % i == 0]) == lst[27] if len(lst) > 27 else False