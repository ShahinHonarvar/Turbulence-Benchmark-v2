def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes):
    if not is_prime(n):
        return False
    for prime in reversed(primes):
        if not prime.startswith(str(n)):
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    if len(numbers_tuple) < 15:
        return []
    x = numbers_tuple[14]
    if is_prime(x):
        primes = [str(p) for p in range(2, x) if is_prime(p)]
        right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, primes)]
        return sorted((int(p) for p in right_truncatable_primes))
    else:
        return []