import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if not 59 <= numbers[61] <= 7000:
        return []
    x = numbers[61]
    primes_up_to_x = [p for p in range(2, x + 1) if is_prime(p)]
    left_right_truncatable_primes = [p for p in primes_up_to_x if is_truncatable_prime(p, primes_up_to_x)]
    return left_right_truncatable_primes