def if_perfect_num(lst):
    if len(lst) > 13:
        return sum([i for i in range(1, lst[13]) if lst[13] % i == 0]) == lst[13] * 2
    return False