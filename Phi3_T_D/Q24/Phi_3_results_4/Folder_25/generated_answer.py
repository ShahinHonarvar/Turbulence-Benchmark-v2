def sum_of_divisors_in_range(n):
    div_sum = 0
    for divisor in range(2, n):
        if n % divisor == 0 and 84 <= divisor <= 86:
            div_sum += divisor
    return div_sum