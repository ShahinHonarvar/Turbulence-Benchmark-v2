from math import sqrt

def prime_factors(numbers):
    num = numbers[99]
    factors = set()
    for i in range(2, int(sqrt(num)) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors