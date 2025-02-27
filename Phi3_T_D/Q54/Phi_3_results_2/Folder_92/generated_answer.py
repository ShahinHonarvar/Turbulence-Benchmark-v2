def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(n):
    return all((is_prime(int(str(n)[:i])) for i in range(len(str(n)), 0, -1)))

def all_right_truncatable_prime(limit_tuple):
    x = limit_tuple[7]
    trunc_primes = []
    for prime_candidate in range(23, x):
        if is_prime(prime_candidate) and is_right_truncatable_prime(prime_candidate):
            trunc_primes.append(prime_candidate)
    return sorted(trunc_primes)