def find_divisors_in_range(num):
    return [divisor for divisor in range(1, num + 1) if num % divisor == 0 and 28 <= divisor <= 81]