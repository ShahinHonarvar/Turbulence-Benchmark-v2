def all_left_right_truncatable_prime(nums):
    """
    Returns a list of all left-and-right-truncatable prime numbers less than or equal to x.
    """
    left_truncatable = [2, 3, 5, 7]
    right_truncatable = [2, 3, 5, 7]
    x = nums[85]
    for i in range(10):
        left_truncatable = [p * 10 + d for p in left_truncatable for d in range(10) if is_prime(p * 10 + d)]
        right_truncatable = [d * 10 + p for p in right_truncatable for d in range(10) if is_prime(d * 10 + p)]
    return sorted(set(left_truncatable) & set(right_truncatable) & set(range(11, x + 1)))

def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True