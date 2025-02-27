import math

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(args: tuple) -> list:
    x = args[0]
    truncatable_primes = []
    for num in range(x):
        is_truncatable = True
        for i in range(len(str(num)) - 1):
            if not is_prime(int(str(num)[i:])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)