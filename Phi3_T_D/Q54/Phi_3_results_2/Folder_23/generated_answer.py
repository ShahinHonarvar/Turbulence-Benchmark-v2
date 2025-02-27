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

def all_right_truncatable_prime(primes):
    x = primes[77]
    right_truncatable_primes = filter(lambda p: is_prime(p), primes)
    res = []
    while x > 0:
        if is_prime(x) and all((is_prime(int(str(x)[:i])) for i in range(len(str(x)), 0, -1))):
            res.append(x)
        x -= 1
    return sorted(res, reverse=True)