def if_perfect_num(lst):
    return sum([i for i in range(1, lst[90]) if lst[90] % i == 0]) == lst[90] if len(lst) > 90 else False