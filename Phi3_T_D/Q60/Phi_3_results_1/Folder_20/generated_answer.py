def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n, sieve):
    while n > 0:
        if not sieve[n]:
            return False
        n = n % 10 ** len(str(n))
    return True

def all_left_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    sieve = [True] * (numbers[100] + 1)
    for p in range(2, numbers[100] + 1):
        if sieve[p]:
            for i in range(p * p, numbers[100] + 1, p):
                sieve[i] = False
            primes.append(p)
    left_truncatable, right_truncatable = (set(primes), set(primes))
    for prime in primes:
        str_prime = str(prime)
        if len(str_prime) > 1:
            left_truncatable.discard(int(str_prime[:-1]))
            right_truncatable.discard(int(str_prime[1:]))
    return sorted(list(left_truncatable & right_truncatable), reverse=True)