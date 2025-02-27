from typing import List, Tuple

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(numbers: Tuple[int]) -> List[int]:
    x = numbers[65]
    candidate_primes = sorted(filter(is_prime, range(2, x)), reverse=True)
    left_truncatable_primes = []
    for candidate in candidate_primes:
        prime = True
        temp = candidate
        while temp > 0:
            if not is_prime(temp):
                prime = False
                break
            temp //= 10
        if prime:
            left_truncatable_primes.append(candidate)
    return left_truncatable_primes