def all_left_truncatable_prime(numbers):
    x = numbers[14]
    return sorted([p for p in range(2, x) if all((int(str(p)[i:]) in prime_sieve(x) for i in range(1, len(str(p)))))], reverse=True)

def prime_sieve(n):
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]