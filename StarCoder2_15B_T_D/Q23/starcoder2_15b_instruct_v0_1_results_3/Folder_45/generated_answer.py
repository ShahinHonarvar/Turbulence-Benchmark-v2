import math

def find_divisors_in_range(n):
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor = i
            quotient = n // i
            if divisor >= 4 and divisor <= 8:
                divisors.append(divisor)
            if quotient >= 4 and quotient <= 8:
                divisors.append(quotient)
    return divisors