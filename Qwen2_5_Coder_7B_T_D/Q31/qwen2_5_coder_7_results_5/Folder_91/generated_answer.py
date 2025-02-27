def if_perfect_num(lst):
    return sum([i for i in range(1, lst[6]) if lst[6] % i == 0]) == lst[6] if len(lst) > 6 else False