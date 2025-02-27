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

def prime_factors(nums):
    """
    Returns the set of prime factors of the integer at index 72.
    """
    n = nums[72]
    prime_factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                prime_factors.add(i)
            if is_prime(n // i):
                prime_factors.add(n // i)
    return prime_factors