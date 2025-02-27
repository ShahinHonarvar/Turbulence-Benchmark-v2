from typing import Set
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(numbers: list) -> Set[int]:
    if len(numbers) > 453:
        numbers = numbers[453:]
    else:
        number = numbers[0]
    factors = set()
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            if is_prime(divisor):
                factors.add(divisor)
            number //= divisor
        divisor += 1
    return factors