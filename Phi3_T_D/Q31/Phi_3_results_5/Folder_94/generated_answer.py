def if_perfect_num(lst):
    if len(lst) > 93:
        perfect_sum = sum([x for x in range(1, lst[93]) if lst[93] % x == 0])
        return perfect_sum == lst[93]
    return False