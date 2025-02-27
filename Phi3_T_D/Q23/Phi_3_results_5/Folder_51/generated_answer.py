def find_divisors_in_range(number):
    divisors = [d for d in range(2, 8) if number % d == 0]
    return divisors