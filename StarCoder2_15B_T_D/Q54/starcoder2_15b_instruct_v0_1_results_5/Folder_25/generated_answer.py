def is_prime(num: int) -> bool:
    """
    Returns True if num is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_right_truncatable(num: int) -> bool:
    """
    Returns True if num is right-truncatable, False otherwise.
    """
    while num > 0:
        if not is_prime(num):
            return False
        num //= 10
    return True

def all_right_truncatable_prime(nums: tuple) -> list:
    """
    Returns a sorted list of all right-truncatable prime numbers less than x, where x is the integer at index 92.
    """
    x = nums[92]
    return sorted([num for num in range(2, x) if is_right_truncatable(num)])