from collections import Counter

def prime_factors(numbers):

    def prime_factors_func(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n = n // i
        if n > 2:
            factors.append(n)
        return factors
    prime_factors_number = prime_factors_func(numbers[23])
    return set(prime_factors_number)