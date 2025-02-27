def if_perfect_num(lst):
    return sum([i for i in range(1, lst[48]) if lst[48] % i == 0]) == lst[48] if len(lst) > 48 else False