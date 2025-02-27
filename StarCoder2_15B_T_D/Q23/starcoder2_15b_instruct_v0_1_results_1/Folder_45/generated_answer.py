def find_divisors_in_range(num):
    divisors = [divisor for divisor in range(4, num + 1) if num % divisor == 0]
    return divisors