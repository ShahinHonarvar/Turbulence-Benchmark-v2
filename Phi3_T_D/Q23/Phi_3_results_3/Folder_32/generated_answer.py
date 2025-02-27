def find_divisors_in_range(number):
    if number <= 0:
        return []
    divisors = [x for x in range(71, 82) if number % x == 0]
    return divisors