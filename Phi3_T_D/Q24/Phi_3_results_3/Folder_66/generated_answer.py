def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Argument must be a positive integer')
    sum_of_divisors = 0
    for i in range(32, 36):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors