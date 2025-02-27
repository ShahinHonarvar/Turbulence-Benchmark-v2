from typing import Tuple

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n: int) -> bool:
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers: Tuple[int]) -> List[int]:
    x = numbers[97]
    return sorted([n for n in range(2, x) if left_truncatable_prime(n)])