from typing import List

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums: tuple) -> List[int]:
    """
    Find all left-and-right-truncatable prime numbers in the given tuple.
    """
    left_right_truncatable_primes = []
    x = nums[32]
    for num in range(2, x + 1):
        if not is_prime(num):
            continue
        num_str = str(num)
        is_truncatable = True
        for i in range(len(num_str) - 1):
            truncated_num = int(num_str[i + 1:])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
            truncated_num = int(num_str[:-i - 1])
            if not is_prime(truncated_num):
                is_truncatable = False
                break
        if is_truncatable:
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)