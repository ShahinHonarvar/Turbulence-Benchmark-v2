def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, sieve):
    return n in sieve and all((is_prime(int(n[i:])) for i in range(len(n))))

def all_left_truncatable_primes(tuple):
    x = tuple[33]
    sieve = [True] * x
    sieve[0] = sieve[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    sieve_set = {i for i, prime in enumerate(sieve) if prime}
    return [i for i in sieve_set if is_left_truncatable_prime(str(i), sieve_set)]