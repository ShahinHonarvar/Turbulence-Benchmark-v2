def find_divisors_in_range(num):
    divisors = [div for div in range(83, 96) if num % div == 0]
    return divisors