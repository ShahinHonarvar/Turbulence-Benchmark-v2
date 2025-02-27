def sum_of_divisors_in_range(n):
    div_sum = sum((i for i in range(28, 82) if n % i == 0))
    return div_sum