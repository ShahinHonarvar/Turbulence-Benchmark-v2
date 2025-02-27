def find_divisors_in_range(number):
    divisors = [x for x in range(658, 869) if number % x == 0]
    return divisors