def all_left_right_truncatable_prime(numbers):
    x = numbers[100]
    truncatable_primes = []
    for prime in primes_sieve(x):
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)

def primes_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, int(limit ** 0.5) + 1):
        if is_prime[prime]:
            for multiple in range(prime * prime, limit + 1, prime):
                is_prime[multiple] = False
    return [prime for prime in range(limit + 1) if is_prime[prime]]

def is_truncatable_prime(prime):
    if prime < 10:
        return prime in (2, 3, 5, 7)
    s = str(prime)
    return s[0] != '0' and s[-1] != '0' and is_truncatable_prime(int(s[1:])) and is_truncatable_prime(int(s[:-1]))