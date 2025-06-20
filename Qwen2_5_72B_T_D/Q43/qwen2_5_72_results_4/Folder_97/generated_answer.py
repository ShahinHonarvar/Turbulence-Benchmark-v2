def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers):
    primes = [num for i, num in enumerate(numbers) if 295 <= i <= 455 and is_prime(num)]
    return sorted(primes, reverse=True)