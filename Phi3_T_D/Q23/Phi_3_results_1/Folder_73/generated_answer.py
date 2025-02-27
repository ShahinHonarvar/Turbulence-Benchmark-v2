def find_divisors_in_range(num):
    divisors = [d for d in range(46, 90) if num % d == 0 and d != 0]
    return divisors