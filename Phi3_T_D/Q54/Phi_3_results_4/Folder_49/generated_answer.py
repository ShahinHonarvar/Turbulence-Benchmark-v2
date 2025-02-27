def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n, primes_set):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[14]
    right_truncatable_primes = []
    sieve = [True] * x
    sieve[0] = sieve[1] = False
    for i in range(2, x):
        if sieve[i - 1]:
            sieve[i * i:x:i] = [False] * len(range(i * i, x, i))
            if is_right_truncatable(i, {j for j in range(2, x) if sieve[j - 1]}):
                right_truncatable_primes.append(i)
    return right_truncatable_primes