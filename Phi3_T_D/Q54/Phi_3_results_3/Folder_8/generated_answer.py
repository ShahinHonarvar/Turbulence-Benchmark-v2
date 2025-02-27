def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(p):
    if not is_prime(p):
        return False
    while p > 0:
        p = int(str(p)[:-1])
        if not is_prime(p):
            return False
    return True

def all_right_truncatable_primes(numbers):
    x = numbers[41]
    return sorted([p for p in range(2, x) if is_right_truncatable_prime(p)], reverse=True)