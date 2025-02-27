def find_divisors_in_range(n):
    divisors = [div for div in range(35, 99) if n % div == 0]
    return divisors