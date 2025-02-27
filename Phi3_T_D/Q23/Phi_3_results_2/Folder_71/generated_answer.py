def find_divisors_in_range(number):
    divisors = [divisor for divisor in range(1, number + 1) if number % divisor == 0 and 45 <= divisor <= 72]
    return divisors