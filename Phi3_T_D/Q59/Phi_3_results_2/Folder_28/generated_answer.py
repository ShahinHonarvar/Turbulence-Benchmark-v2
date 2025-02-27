from typing import List, Tuple

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(max_value: int) -> List[int]:
    primes = [i for i in range(11, max_value) if is_prime(i)]
    extended_primes = []
    for prime in primes:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not is_prime(int(str_prime[i:])):
                break
        else:
            extended_primes.append(prime)
    return extended_primes

def all_left_truncatable_prime(numbers_tuple: Tuple[int]) -> List[int]:
    x = numbers_tuple[19]
    return left_truncatable_primes(x)