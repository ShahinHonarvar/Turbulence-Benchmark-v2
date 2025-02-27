def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_zero(n):
    return '0' in str(n)

def is_truncatable(n, prime_set):
    s = str(n)
    for i in range(1, len(s) // 2 + 1):
        if not (is_prime(int(s[i:])) and is_prime(int(s[:-i or None])) and (not has_zero(int(s[i:]))) and (not has_zero(int(s[:-i or None])))):
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[46]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    prime_set = set(primes)
    truncatable_primes = [p for p in primes if is_truncatable(p, prime_set)]
    return sorted(truncatable_primes, reverse=True)