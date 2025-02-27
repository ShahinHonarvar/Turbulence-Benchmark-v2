def find_divisors_in_range(number):
    divisors = [i for i in range(48, 63) if number % i == 0]
    return divisors