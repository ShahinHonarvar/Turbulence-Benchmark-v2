def sum_of_divisors_in_range(num):
    if num < 1:
        raise ValueError('Argument must be a positive integer')
    divisors = [d for d in range(1, num + 1) if num % d == 0 and d >= 11 and (d <= 41)]
    if not divisors:
        return 0
    return sum(divisors)