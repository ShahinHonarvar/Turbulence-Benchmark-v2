def find_divisors_in_range(num):
    return [divisor for divisor in range(13, 63) if num % divisor == 0]