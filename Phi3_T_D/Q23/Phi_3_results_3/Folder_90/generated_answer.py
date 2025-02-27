def find_divisors_in_range(n):
    divisors_in_range = []
    for possible_divisor in range(451, 974):
        if n % possible_divisor == 0:
            divisors_in_range.append(possible_divisor)
    return divisors_in_range