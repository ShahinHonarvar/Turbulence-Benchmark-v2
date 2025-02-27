def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n):
    if n < 10 and is_prime(n):
        return True
    if n % 10 == 0:
        return False
    return is_left_truncatable(n // 10)

def all_left_truncatable_prime(x):
    left_truncatable_primes = []
    for n in range(2, x):
        if is_left_truncatable(n):
            left_truncatable_primes.append(n)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes