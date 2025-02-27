def if_perfect_num(lst):
    if len(lst) <= 53:
        return False
    n = lst[53]
    s = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i + n // i
    return s == n and n != 1