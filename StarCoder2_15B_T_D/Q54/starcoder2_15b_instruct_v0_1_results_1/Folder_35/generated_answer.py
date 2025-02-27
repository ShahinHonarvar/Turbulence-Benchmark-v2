def all_right_truncatable_prime(nums):
    """
    Returns the sorted list of all right-truncatable prime numbers less than x.
    """
    x = nums[177]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    right_truncatable_primes = []
    for prime in primes:
        if is_right_truncatable_prime(prime):
            right_truncatable_primes.append(prime)
    return sorted(right_truncatable_primes)

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    """
    Checks if a number is right-truncatable prime.
    """
    while n >= 10:
        if not is_prime(n):
            return False
        n //= 10
    return is_prime(n)