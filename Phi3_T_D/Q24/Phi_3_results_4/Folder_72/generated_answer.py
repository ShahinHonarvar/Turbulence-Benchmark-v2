def sum_of_divisors_in_range(n):
    if n <= 32:
        return 0
    sum_div = 0
    for i in range(32, 91):
        if n % i == 0:
            sum_div += i
    return sum_div