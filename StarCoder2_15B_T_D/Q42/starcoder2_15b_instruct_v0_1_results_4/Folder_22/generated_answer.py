def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors = []
    for i, num in enumerate(numbers):
        if i == 72:
            for j in range(2, num + 1):
                if num % j == 0 and is_prime(j):
                    prime_factors.append(j)
    return set(prime_factors)