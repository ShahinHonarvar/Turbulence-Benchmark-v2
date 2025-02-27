def find_divisors_in_range(n):
    return [x for x in range(1, int(n ** 0.5) + 1) if n % x == 0 and 5 <= x * x <= 81]