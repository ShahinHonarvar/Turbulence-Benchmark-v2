def if_perfect_num(lst):
    return sum([i for i in range(1, lst[43]) if lst[43] % i == 0]) == lst[43] if len(lst) > 43 else False