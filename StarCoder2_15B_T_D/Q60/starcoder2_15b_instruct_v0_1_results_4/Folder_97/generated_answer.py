def all_left_right_truncatable_prime(nums):
    """
    Returns a list of all left-and-right-truncatable prime numbers less than or equal to
    the integer at index 645 in the given tuple of positive integers.
    """
    x = nums[645]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    """
    Checks if a given number is a prime number.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    """
    Checks if a given number is a left-and-right-truncatable prime number.
    """
    if n < 10:
        return is_prime(n)
    if not is_prime(n):
        return False
    return is_left_right_truncatable_prime(int(str(n)[1:])) and is_left_right_truncatable_prime(int(str(n)[:-1]))