from typing import List

def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_between_indices(nums: List[int]) -> List[int]:
    """
    Finds the sorted list of all prime numbers from index 61 to index 80, both inclusive.
    If no prime number exists in the specified range, returns an empty list.
    """
    primes = []
    for i, num in enumerate(nums):
        if is_prime(num) and 61 <= i <= 80:
            primes.append(num)
    primes.sort(reverse=True)
    return primes