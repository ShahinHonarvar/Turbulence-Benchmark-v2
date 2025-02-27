from collections import Counter
import math

def prime_factors(numbers):

    def factors(n):
        primes = []
        while n % 2 == 0:
            primes.append(2)
            n //= 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                primes.append(i)
                n //= i
        if n > 2:
            primes.append(n)
        return primes
    return factors(numbers[94]) if len(numbers) > 94 else 'Index out of range'