def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, is_prime_cache):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime_cache(int(str_n[i:])) or not is_prime_cache(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(range_end):
    prime_cache = {2, 3, 5, 7}
    truncatable_primes = set()
    for i in range(3, range_end + 1, 2):
        if i not in prime_cache and is_prime(i):
            prime_cache.add(i)
            if is_truncatable(i, prime_cache.__contains__):
                truncatable_primes.add(i)
    return sorted(truncatable_primes, reverse=True)