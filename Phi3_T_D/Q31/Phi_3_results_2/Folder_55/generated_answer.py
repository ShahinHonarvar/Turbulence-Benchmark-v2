def if_perfect_num(lst):
    if 21 < len(lst) and sum((i for i in range(1, lst[21]) if lst[21] % i == 0)) == 2 * lst[21]:
        return True
    return False