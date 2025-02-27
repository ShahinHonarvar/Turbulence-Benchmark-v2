def find_divisors_in_range(number):
    divisors_in_range = [x for x in range(number, 0, -1) if 6 <= x <= 8 and number % x == 0]
    return divisors_in_range