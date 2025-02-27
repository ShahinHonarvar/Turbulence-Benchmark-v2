import math
from itertools import islice

def prime_factors(numbers):
    prime_factors = []
    for number in islice(numbers, 80, 81):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                if math.isprime(i):
                    prime_factors.append(i)
                if math.isprime(number // i):
                    prime_factors.append(number // i)
    return set(prime_factors)