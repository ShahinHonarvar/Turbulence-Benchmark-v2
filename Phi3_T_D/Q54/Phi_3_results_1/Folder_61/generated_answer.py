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

def is_right_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(params):
    x = params[3]
    max_digits = len(str(x - 1))
    primes = (n for n in range(2, x) if is_prime(n))
    right_truncatable_primes = [p for p in primes if all((is_prime(p // 10 ** i) for i in range(max_digits)))]
    return sorted(right_truncatable_primes, reverse=True)