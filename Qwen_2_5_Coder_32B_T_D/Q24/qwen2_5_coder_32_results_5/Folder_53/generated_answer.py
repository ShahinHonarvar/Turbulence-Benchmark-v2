def sum_of_divisors_in_range(n):
    s = 0
    for i in range(4, 10):
        if n % i == 0:
            s += i
    return s