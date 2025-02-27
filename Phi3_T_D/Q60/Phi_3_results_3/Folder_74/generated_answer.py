def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, primes):
    if n not in primes:
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if is_prime(int(str_n[i:])) or is_prime(int(str_n[:-i])):
            continue
        return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[36]
    primes = [n for n in range(2, x + 1) if is_prime(n)]
    truncatable_primes = [p for p in primes if is_truncatable_prime(p, primes)]
    return sorted(truncatable_primes)