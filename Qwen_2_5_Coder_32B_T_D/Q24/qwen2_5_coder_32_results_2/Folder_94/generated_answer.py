def sum_of_divisors_in_range(n):
    s = 0
    for d in range(35, 38):
        if n % d == 0:
            s += d
    return s