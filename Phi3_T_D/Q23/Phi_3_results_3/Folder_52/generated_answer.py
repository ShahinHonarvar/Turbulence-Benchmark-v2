def find_divisors_in_range(n):
    return [divisor for divisor in range(70, 73) if n % divisor == 0 and n != divisor]