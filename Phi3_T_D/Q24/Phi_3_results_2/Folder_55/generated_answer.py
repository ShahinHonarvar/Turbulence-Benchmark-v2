def sum_of_divisors_in_range(n):
    if n < 1:
        raise ValueError('n must be a positive integer')
    divisors_sum = 0
    for i in range(5, 9):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum