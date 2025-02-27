import math

def prime_factors(numbers):
    if len(numbers) <= 73:
        raise ValueError('The input list must contain at least 74 elements.')
    n = numbers[73]
    prime_factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime_factors.add(i)
    return prime_factors