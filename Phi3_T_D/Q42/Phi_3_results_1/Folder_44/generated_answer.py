def prime_factors(numbers):

    def prime_factor(num):
        factors = set()
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 1:
            factors.add(num)
        return factors
    if 828 < len(numbers):
        return prime_factor(numbers[828])
    else:
        return 'Index out of bounds'