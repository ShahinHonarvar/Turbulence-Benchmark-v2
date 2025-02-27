def find_divisors_in_range(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError('The argument must be a positive integer.')
    divisors = [x for x in range(744, 886) if number % x == 0]
    return divisors