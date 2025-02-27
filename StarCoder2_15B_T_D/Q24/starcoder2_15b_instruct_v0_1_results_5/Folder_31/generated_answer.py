def sum_of_divisors_in_range(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    filtered_divisors = [divisor for divisor in divisors if 35 <= divisor <= 55]
    return sum(filtered_divisors) if filtered_divisors else 0