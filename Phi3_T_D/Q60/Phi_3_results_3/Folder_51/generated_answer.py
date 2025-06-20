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

def is_left_right_truncatable_prime(n, primes):
    if n not in primes:
        return False
    str_n = str(n)
    while len(str_n) > 1:
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[1:-1]
    return True

def all_left_right_truncatable_primes(limit_range):
    primes = [n for n in range(2, limit_range + 1) if is_prime(n)]
    return [p for p in primes if is_left_right_truncatable_prime(p, primes)]