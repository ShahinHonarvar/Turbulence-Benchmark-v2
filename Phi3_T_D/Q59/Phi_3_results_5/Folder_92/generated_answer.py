def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    if n not in primes:
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_left_truncatable_prime(params):
    x = params[7]
    primes = [2, 3, 5, 7]
    truncatable_primes = []
    for prime in primes:
        if prime < x and is_left_truncatable_prime(prime, primes):
            truncatable_primes.append(prime)
    return truncatable_primes