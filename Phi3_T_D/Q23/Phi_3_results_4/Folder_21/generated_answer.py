def find_divisors_in_range(num):
    divisors_in_range = [divisor for divisor in range(120, 350) if num % divisor == 0]
    return divisors_in_range