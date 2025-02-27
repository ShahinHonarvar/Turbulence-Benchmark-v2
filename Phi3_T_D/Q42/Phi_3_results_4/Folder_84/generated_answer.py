from math import sqrt

def prime_factors(numbers):
    if len(numbers) <= 685 or numbers[685] <= 1:
        return set()

    def find_factors(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    return find_factors(numbers[685])