def sieve_of_eratosthenes(n):
    primes = [True for i in range(n + 1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def all_left_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[42]
    primes = sieve_of_eratosthenes(x)
    left_truncatable_primes = []
    for i in range(x):
        is_left_truncatable = True
        num = i
        while num > 0:
            digit = num % 10
            if digit == 0 or not primes[num]:
                is_left_truncatable = False
                break
            num //= 10
        if is_left_truncatable:
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)