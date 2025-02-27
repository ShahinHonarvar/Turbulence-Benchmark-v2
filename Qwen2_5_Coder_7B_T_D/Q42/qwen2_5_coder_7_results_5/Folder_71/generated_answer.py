def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) > 78:
        target = numbers[78]
        factors = set()
        for i in range(2, target + 1):
            while target % i == 0:
                if is_prime(i):
                    factors.add(i)
                target //= i
        return factors
    else:
        return 'Index out of range'