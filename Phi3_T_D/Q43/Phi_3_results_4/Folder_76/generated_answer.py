from typing import List

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers: List[int]) -> List[int]:
    start, end = (149, 979)
    return sorted([num for num in numbers[start:end + 1] if is_prime(num)])