import math

def is_left_truncatable_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    if n > 10 and n % 10 == 0:
        return False
    if n < 10:
        return True
    return is_left_truncatable_prime(n // 10)

def all_left_truncatable_prime(t):
    x = t[81]
    prime_numbers = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    return sorted(prime_numbers, reverse=True)