def find_divisors_in_range(num):
    divisors = [divisor for divisor in range(3, 8) if num % divisor == 0]
    return divisors