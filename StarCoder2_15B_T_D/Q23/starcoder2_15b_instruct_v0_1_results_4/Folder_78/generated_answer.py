def find_divisors_in_range(number):
    divisors = [divisor for divisor in range(1, number + 1) if number % divisor == 0]
    return [divisor for divisor in divisors if 20 <= divisor <= 50]