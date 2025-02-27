def sum_of_divisors_in_range(number):
    divisors = [divisor for divisor in range(1, number + 1) if number % divisor == 0]
    divisors_in_range = [divisor for divisor in divisors if 35 <= divisor <= 98]
    return sum(divisors_in_range)