from typing import List

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(numbers: List[int]) -> List[int]:
    primes = [x for x in numbers[36:96] if is_prime(x)]
    return sorted(primes, reverse=True)