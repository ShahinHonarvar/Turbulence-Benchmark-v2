import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = [n for n in numbers if is_prime(n)]
    left_truncatable = [n for n in primes if n >= 10 and is_prime(n // 10)]
    right_truncatable = [n for n in primes if n >= 10 and is_prime(n % 10)]
    truncatable = [n for n in primes if n in left_truncatable and n in right_truncatable]
    truncatable.sort(reverse=True)
    return truncatable