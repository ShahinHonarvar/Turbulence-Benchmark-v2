def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [n for i, n in enumerate(numbers) if 46 <= i <= 61 and is_prime(n)]
    primes.sort()
    return primes