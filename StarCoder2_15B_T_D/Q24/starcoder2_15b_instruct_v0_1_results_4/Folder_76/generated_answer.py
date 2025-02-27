def sum_of_divisors_in_range(num):
    if num < 1:
        raise ValueError('The argument must be a positive integer.')
    divisors = [i for i in range(744, 886) if num % i == 0]
    if len(divisors) == 0:
        return 0
    else:
        return sum(divisors)