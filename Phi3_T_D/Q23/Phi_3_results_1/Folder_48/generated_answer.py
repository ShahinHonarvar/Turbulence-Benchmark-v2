def find_divisors_in_range(num):
    return [divisor for divisor in range(461, 828) if divisor != 0 and num % divisor == 0]