def if_perfect_num(lst):
    if len(lst) > 714:
        n = lst[714]
        return n == sum((i for i in range(1, n) if n % i == 0))
    return False