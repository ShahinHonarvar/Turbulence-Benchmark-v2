def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    """Check if a number is a right-truncatable prime."""
    return all((is_prime(int(str(n)[:i])) for i in range(1, len(str(n)) + 1))) and is_prime(n)

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i, right_truncatable_primes):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)