def if_perfect_num(lst):
    if len(lst) < 91:
        return False
    n = lst[90]
    s = sum([i for i in range(1, n) if n % i == 0])
    return s == n