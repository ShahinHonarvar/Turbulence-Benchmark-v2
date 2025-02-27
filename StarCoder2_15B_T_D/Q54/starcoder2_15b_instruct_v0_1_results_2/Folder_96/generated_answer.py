from typing import List, Tuple

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums: Tuple[int, ...]) -> List[int]:
    """
    Find all right-truncatable prime numbers in a tuple of positive integers.
    A right-truncatable prime number is a prime number that remains prime when
    the last rightmost digit is successively removed.
    """
    result = []
    x = nums[29]
    for i in range(2, x):
        n = i
        while n > 0:
            if is_prime(n):
                result.append(n)
                break
            n //= 10
    return sorted(result)