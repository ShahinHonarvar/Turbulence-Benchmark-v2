def if_perfect_num(lst):
    if len(lst) <= 74:
        return False
    n = lst[74]
    return n == sum((x for x in range(1, n) if n % x == 0))