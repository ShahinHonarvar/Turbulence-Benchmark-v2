def all_left_truncatable_prime(numbers):
    x = numbers[29]
    sieve = [True] * x
    sieve[0:2] = [False, False]
    for i in range(2, int(x ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, x, i):
                sieve[j] = False
    primes = [i for i in range(2, x) if sieve[i] and '0' not in str(i)]
    left_truncatable_primes = []
    for prime in primes:
        str_prime = str(prime)
        is_left_truncatable = True
        for i in range(len(str_prime)):
            if not sieve[int(str_prime[i:])]:
                is_left_truncatable = False
                break
        if is_left_truncatable:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)