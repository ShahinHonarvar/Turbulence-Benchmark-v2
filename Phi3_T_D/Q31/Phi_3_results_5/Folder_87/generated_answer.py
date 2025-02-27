def if_perfect_num(lst):
    return sum((i for i in range(1, lst[95] if len(lst) > 96 else 1) if lst[95] % i == 0)) == lst[95]