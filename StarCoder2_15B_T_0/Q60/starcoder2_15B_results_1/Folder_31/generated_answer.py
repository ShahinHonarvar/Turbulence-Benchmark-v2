def all_left_right_truncatable_prime(numbers):
    x = numbers[50]
    truncatable_primes = []
    for prime in primes_sieve(x):
        if is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)

def primes_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]

def is_truncatable_prime(prime):
    if prime < 10:
        return False
    if prime in [2, 3, 5, 7]:
        return True
    prime_str = str(prime)
    if '0' in prime_str:
        return False
    for i in range(1, len(prime_str)):
        if not is_prime(int(prime_str[i:])):
            return False
        if not is_prime(int(prime_str[:i])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    if n in [2, 3]:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True