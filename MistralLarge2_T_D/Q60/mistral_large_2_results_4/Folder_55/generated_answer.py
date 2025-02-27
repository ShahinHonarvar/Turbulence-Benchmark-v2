def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(n):
    if not is_prime(n):
        return False
    if '0' in str(n):
        return False
    while len(str(n)) > 1:
        n = int(str(n)[1:-1])
        if not is_prime(n):
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[73]
    primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(primes, reverse=True)