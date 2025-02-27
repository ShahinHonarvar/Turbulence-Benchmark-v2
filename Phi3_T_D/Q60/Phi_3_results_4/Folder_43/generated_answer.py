def is_truncatable_prime(p, primes_set):
    if p not in primes_set:
        return False
    str_p = str(p)
    for i in range(1, len(str_p)):
        if not int(str_p[i:]) in primes_set or not int(str_p[:-i]) in primes_set:
            return False
    return True

def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[89]
    primes = set()
    truncatable_primes = []
    for p in range(2, x + 1):
        if all((p % d != 0 for d in range(2, int(p ** 0.5) + 1))):
            primes.add(p)
            if is_truncatable_prime(p, primes):
                truncatable_primes.append(p)
    return sorted(truncatable_primes, reverse=True)