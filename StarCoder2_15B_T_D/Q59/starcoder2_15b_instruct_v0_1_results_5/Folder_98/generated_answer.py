def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    if n < 10:
        return True
    return is_left_truncatable_prime(int(str(n)[1:]))

def get_left_truncations(n):
    truncations = []
    while n > 0:
        truncations.append(n)
        n //= 10
    return truncations

def all_left_truncatable_prime(t):
    x = t[8]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes