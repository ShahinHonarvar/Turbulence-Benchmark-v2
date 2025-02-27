def sum_of_divisors_in_range(n):
    if n < 1:
        raise ValueError('Argument must be a positive integer')
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0 and 46 <= i <= 65:
            sum_of_divisors += i
    return sum_of_divisors