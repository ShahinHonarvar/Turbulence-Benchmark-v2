def prime_sieve(n):
    primes = [True for i in range(n + 1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    primes = prime_sieve(x)
    truncatable_primes = []
    for i in range(10, x + 1):
        if primes[i] and (not str(i).startswith('0')):
            is_truncatable = True
            for j in range(1, len(str(i))):
                if not primes[int(str(i)[j:])] or not primes[int(str(i)[:-j])]:
                    is_truncatable = False
                    break
            if is_truncatable:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes