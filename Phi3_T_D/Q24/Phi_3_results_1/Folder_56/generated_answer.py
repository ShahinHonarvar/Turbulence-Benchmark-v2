def sum_of_divisors_in_range(n):
    s = 0
    for k in range(6, 10):
        if n % k == 0:
            s += k
    return s