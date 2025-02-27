def find_divisors_in_range(number):
    divisors = []
    for possible_divisor in range(451, 974):
        if number % possible_divisor == 0:
            divisors.append(possible_divisor)
    return divisors