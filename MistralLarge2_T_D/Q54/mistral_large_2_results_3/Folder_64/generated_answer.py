def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[4]
    primes = [2, 3, 5, 7]
    truncatable_primes = []

    def truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    for prime in primes:
        if prime < x and truncatable(prime):
            truncatable_primes.append(prime)
    for i in range(1, x):
        for j in range(len(primes)):
            candidate = primes[j] * 10 + i
            if candidate < x and is_prime(candidate) and truncatable(candidate):
                primes.append(candidate)
                truncatable_primes.append(candidate)
    return sorted(truncatable_primes)