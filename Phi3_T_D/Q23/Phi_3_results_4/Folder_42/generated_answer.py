def find_divisors_in_range(number):
    divisors = [div for div in range(14, 94) if number % div == 0]
    return divisors