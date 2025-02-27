def if_perfect_num(lst):
    if len(lst) > 828:
        n = lst[828]
        return n == sum((x for x in range(1, n) if n % x == 0))
    return False