import math

def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor = i
            quotient = n // i
            if divisor >= 14 and divisor <= 93:
                sum_of_divisors += divisor
            if quotient >= 14 and quotient <= 93:
                sum_of_divisors += quotient
    return sum_of_divisors