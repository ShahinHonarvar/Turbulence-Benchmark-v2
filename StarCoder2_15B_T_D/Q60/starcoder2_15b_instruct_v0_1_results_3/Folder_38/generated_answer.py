def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    return is_prime(n) and is_truncatable_prime(n // 10) and is_truncatable_prime(n % 10)

def all_left_right_truncatable_prime(t):
    x = t[28]
    truncatable_primes = []
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    truncatable_primes.sort()
    return truncatable_primes