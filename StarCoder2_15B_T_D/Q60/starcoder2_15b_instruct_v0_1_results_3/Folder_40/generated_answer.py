def all_left_right_truncatable_prime(tup: tuple) -> list:
    x = tup[0]
    primes = []
    for n in range(2, x + 1):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    truncatable_primes = []
    for prime in primes:
        is_truncatable = True
        prime_str = str(prime)
        for i in range(len(prime_str)):
            truncated_prime = int(prime_str[i:])
            if truncated_prime not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes