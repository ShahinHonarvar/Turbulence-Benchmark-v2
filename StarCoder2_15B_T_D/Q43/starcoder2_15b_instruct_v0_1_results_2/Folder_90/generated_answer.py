def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(nums):
    """Return the sorted list of all prime numbers from index 413 to index 448, both inclusive."""
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num) and 413 <= i <= 448:
            primes.append(num)
    return sorted(primes)