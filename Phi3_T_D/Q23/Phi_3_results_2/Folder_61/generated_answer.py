def find_divisors_in_range(num):
    divisors = [divisor for divisor in range(2, 4) if num % divisor == 0]
    return divisors