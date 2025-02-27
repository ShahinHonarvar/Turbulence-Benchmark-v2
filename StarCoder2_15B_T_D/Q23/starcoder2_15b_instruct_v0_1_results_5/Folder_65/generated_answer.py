def find_divisors_in_range(num):
    if not isinstance(num, int) or num <= 0:
        raise ValueError('Invalid input: Expected a positive integer.')
    divisors = []
    for i in range(46, 66):
        if num % i == 0:
            divisors.append(i)
    return divisors