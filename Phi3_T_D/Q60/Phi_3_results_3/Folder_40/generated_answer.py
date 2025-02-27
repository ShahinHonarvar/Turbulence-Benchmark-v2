def is_left_right_truncatable(n, primes):
    while n > 0:
        if not is_prime(n, primes):
            return False
        if str(n)[0] == '0' or str(n)[-1] == '0':
            return False
        n = int(str(n)[1:-1])
    return True

def all_left_right_truncatable_prime(tup):
    max_val = tup[10]
    primes = set(sieve_of_eratosthenes(max_val))
    res = [p for p in primes if is_left_right_truncatable(p, primes)]
    return sorted(res, reverse=True)