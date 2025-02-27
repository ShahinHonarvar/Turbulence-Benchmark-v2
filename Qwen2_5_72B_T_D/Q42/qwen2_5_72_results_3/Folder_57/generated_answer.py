def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers):
    value = numbers[92]
    factors = set()
    for i in range(2, value + 1):
        if value % i == 0 and is_prime(i):
            factors.add(i)
    return factors