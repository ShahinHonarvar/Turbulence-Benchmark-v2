def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(numbers) <= 6:
        return set()
    prime_factors = set()
    for i in range(2, numbers[6] // 2 + 1):
        if numbers[6] % i == 0 and is_prime(i):
            prime_factors.add(i)
    return prime_factors