def find_divisors_in_range(n):
    divisors = [x for x in range(2, 5) if n % x == 0]
    return divisors