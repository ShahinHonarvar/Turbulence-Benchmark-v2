def sum_of_divisors_in_range(n):
    if n <= 0:
        raise ValueError('The input must be a positive integer.')
    sum_of_divisors = 0
    for i in range(1, n + 1):
        if n % i == 0 and 3 <= i <= 9:
            sum_of_divisors += i
    return sum_of_divisors