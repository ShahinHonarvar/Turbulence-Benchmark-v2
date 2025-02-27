def if_perfect_num(lst):
    if len(lst) > 37:
        n = lst[37]
        s = sum((i for i in range(1, n) if n % i == 0))
        return s == n
    return False