def is_left_right_truncatable_prime(n):
    """
    Check if a number is left-and-right-truncatable prime.
    """
    if n < 10:
        return n in (2, 3, 5, 7)
    if n % 10 == 0 or not is_prime(n):
        return False
    return is_left_right_truncatable_prime(n // 10)

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    """
    Find all left-and-right-truncatable prime numbers in a given range.
    """
    x = nums[96]
    return sorted(filter(is_left_right_truncatable_prime, range(1, x + 1)), reverse=True)