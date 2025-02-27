def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_set):
    if n < 10:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def generate_primes(n):
    primes = [False, False] + [True] * (n - 1)
    for p in range(2, int(n ** 0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
    return [p for p, prime in enumerate(primes) if prime and p >= 10]

def all_right_truncatable_prime(numbers):
    x = numbers[126]
    primes = generate_primes(x)
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, set(primes))]
    return sorted(right_truncatable_primes, reverse=True)