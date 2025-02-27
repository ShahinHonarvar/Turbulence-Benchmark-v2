def if_perfect_num(lst):
    if len(lst) <= 312:
        return False
    n = lst[312]
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n