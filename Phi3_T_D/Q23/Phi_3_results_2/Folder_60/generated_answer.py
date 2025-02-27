def find_divisors_in_range(n):
    divisors = [divisor for divisor in range(41, 56) if n % divisor == 0]
    return divisors