def find_divisors_in_range(num):
    divisors = [divisor for divisor in range(3, min(eight, num + 1)) if num % divisor == 0]
    return divisors