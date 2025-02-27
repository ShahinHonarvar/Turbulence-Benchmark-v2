import sympy
from typing import List, Tuple

def all_left_right_truncatable_prime(numbers: Tuple[int, ...]) -> List[int]:
    x = numbers[992]
    truncatable_primes = []
    for num in range(2, x + 1):
        if all((sympy.isprime(int(str(num)[:i])) and sympy.isprime(int(str(num)[i:])) for i in range(1, len(str(num))))):
            if '0' not in str(num):
                truncatable_primes.append(num)
    return sorted(truncatable_primes)