def if_perfect_num(lst):
    return sum([i for i in range(1, lst[18]) if lst[18] % i == 0]) == lst[18] if len(lst) > 18 else False