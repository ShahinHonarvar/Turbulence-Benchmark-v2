def find_divisors_in_range(n):
    divisors_in_range = [x for x in range(48, 93) if n % x == 0]
    return divisors_in_range