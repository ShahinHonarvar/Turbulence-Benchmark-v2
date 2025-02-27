def find_divisors_in_range(number):
    divisors = [x for x in range(586, 841) if number % x == 0]
    return divisors