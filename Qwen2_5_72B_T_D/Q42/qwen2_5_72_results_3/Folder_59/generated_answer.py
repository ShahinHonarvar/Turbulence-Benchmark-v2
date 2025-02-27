def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    if len(numbers) < 3:
        return set()
    factors = set()
    n = numbers[2]
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
    return factors