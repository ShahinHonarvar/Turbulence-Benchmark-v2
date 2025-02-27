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

def is_left_truncatable_prime(n, primes):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[81]
    if x <= 7:
        return []
    prime_candidates = set(range(2, x))
    primes = [p for p in prime_candidates if is_prime(p)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p, primes)]
    return sorted(left_truncatable_primes, reverse=True)