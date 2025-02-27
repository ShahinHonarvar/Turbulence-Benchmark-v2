def find_divisors_in_range(num):
    return [div for div in range(71, 82) if num % div == 0 and div != 0]