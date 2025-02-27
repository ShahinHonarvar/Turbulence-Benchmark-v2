def find_divisors_in_range(n):
    divisors = [div for div in range(14, 94) if n % div == 0]
    return divisors