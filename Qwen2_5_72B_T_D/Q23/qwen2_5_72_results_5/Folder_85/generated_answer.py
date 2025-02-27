def find_divisors_in_range(n):
    divisors = [x for x in range(2, 6) if n % x == 0]
    return divisors