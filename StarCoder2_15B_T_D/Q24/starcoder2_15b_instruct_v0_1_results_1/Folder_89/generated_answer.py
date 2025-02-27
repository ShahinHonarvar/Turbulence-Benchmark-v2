def sum_of_divisors_in_range(num: int) -> int:
    sum_of_divisors = 0
    for divisor in range(1, num + 1):
        if 14 <= divisor <= 48 and num % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors