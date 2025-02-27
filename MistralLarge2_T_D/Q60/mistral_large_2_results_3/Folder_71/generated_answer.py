def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    while n_str:
        if not is_prime(int(n_str)):
            return False
        n_str = n_str[1:-1]
    return True

def all_left_right_truncatable_prime(t):
    x = t[22]
    truncatable_primes = [n for n in range(2, x + 1) if is_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)