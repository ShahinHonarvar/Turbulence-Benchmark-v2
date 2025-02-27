def all_left_truncatable_prime(numbers):
    x = numbers[792]
    sieve = [True] * x
    sieve[0] = sieve[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    primes = [i for i in range(2, x) if sieve[i] and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        while prime > 0:
            if not sieve[prime]:
                break
            prime //= 10
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)