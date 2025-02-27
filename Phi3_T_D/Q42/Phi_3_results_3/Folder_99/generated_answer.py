from math import sqrt
from typing import Set

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(nums: list) -> Set[int]:
    n = nums[733] if 733 < len(nums) else None
    if n is None or not isinstance(n, int) or n <= 1:
        return set()
    factors = set()
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.add(i)
    return factors