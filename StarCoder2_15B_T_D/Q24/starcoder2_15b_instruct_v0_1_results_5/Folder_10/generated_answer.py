def sum_of_divisors_in_range(num):
    assert num > 0, 'The input must be a positive integer'
    divisors = [d for d in range(1, num + 1) if num % d == 0 and d >= 60 and (d <= 86)]
    return sum(divisors) if divisors else 0