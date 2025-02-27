def sum_of_divisors_in_range(n):
    divisors = [1, 2, 3, 4, 5, 6, 7]
    sum_divisors = 0
    for d in divisors:
        if n % d == 0:
            sum_divisors += d
    return sum_divisors