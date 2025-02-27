def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Argument must be a positive integer.')
    total = 0
    for i in range(586, 841):
        if n % i == 0:
            total += i
    return total