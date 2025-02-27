def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factorize(num):
        factors = set()
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.add(d)
                num //= d
            d += 1
        if num > 1:
            factors.add(num)
        return factors
    if len(numbers) < 11:
        return set()
    return factorize(numbers[10])