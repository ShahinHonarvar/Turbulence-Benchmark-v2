def find_divisors_in_range(n):
    divisors = [div for div in range(20, min(51, n + 1)) if n % div == 0]
    return divisors