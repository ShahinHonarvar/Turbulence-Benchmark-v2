def find_divisors_in_range(number):
    divisors = [div for div in range(10, 70) if number % div == 0]
    return divisors