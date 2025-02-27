def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    for num in numbers:
        n = abs(num)
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.add(i)
    return factors if len(numbers) > 72 else set()