def find_divisors_in_range(number):
    divisors = [x for x in range(4, 7) if number % x == 0]
    return divisors