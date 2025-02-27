def find_divisors_in_range(number):
    divisors = [divisor for divisor in range(1, number + 1) if divisor > 49 and divisor <= 81 and (number % divisor == 0)]
    return divisors