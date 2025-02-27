def prime_factors(numbers):
    if len(numbers) <= 84:
        n = numbers[84]
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 1:
            factors.add(n)
        return factors
    else:
        raise IndexError('List index out of range')