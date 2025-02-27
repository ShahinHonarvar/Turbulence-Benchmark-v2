def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    sieve = [True] * (lst[263] + 1)
    p = 2
    while p * p <= lst[263]:
        if sieve[p]:
            for i in range(p * p, len(sieve), p):
                sieve[i] = False
        p += 1
    prime_factors_set = {p for p in range(2, lst[263] + 1) if sieve[p] and lst[263] % p == 0}
    return prime_factors_set