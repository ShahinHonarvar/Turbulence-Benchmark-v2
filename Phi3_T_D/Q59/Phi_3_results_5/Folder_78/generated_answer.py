def all_left_truncatable_prime(tup):
    primes_lt = sorted(filter(lambda p: all((is_prime(int(p[i:])) for i in range(len(str(p))))), (str(p) for p in range(2, tup[23]) if '0' not in str(p))))
    return primes_lt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True