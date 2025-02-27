def find_divisors_in_range(num):
    return [divisor for divisor in range(15, 93) if num % divisor == 0]