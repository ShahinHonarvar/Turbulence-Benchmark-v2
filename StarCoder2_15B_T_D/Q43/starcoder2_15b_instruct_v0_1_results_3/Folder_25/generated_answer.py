def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    return sorted([n for i, n in enumerate(numbers) if is_prime(n) and 52 <= i <= 53])