def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    while n_str:
        if not is_prime(int(n_str)):
            return False
        n_str = n_str[1:]
    return True

def all_left_truncatable_prime(tup):
    x = tup[88]
    primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(primes, reverse=True)