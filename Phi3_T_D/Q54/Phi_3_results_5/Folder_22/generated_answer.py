def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(n):
    primes = []
    sieve = [False] * (n + 1)
    for i in range(2, n + 1):
        if not sieve[i]:
            primes.append(i)
            for j in range(i * 2, n + 1, i):
                sieve[j] = True
    right_truncs = [str(p) for p in primes if all((is_prime(int(p[i:])) for i in range(len(str(p)))))]
    return right_truncs

def all_right_truncatable_prime(numbers):
    x = numbers[85]
    return sorted(right_truncatable_primes(x))