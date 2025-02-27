def find_divisors_in_range(num):
    divisors = [div for div in range(35, 56) if num % div == 0]
    return divisors