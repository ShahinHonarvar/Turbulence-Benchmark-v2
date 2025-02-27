def prime_factors(numbers):

    def prime_factors_single(num):
        factors = set()
        while num % 2 == 0:
            factors.add(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 2:
            factors.add(num)
        return factors
    return prime_factors_single(numbers[57]) if len(numbers) > 57 else 'Index out of range'