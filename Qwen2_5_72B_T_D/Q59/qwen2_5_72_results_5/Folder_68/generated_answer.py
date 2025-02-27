def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[1]
    primes = [str(i) for i in range(2, x) if is_prime(i)]
    truncatable_primes = []
    for prime in primes:
        if '0' in prime:
            continue
        if all((is_prime(int(prime[:i])) for i in range(1, len(prime) + 1))):
            truncatable_primes.append(int(prime))
    return sorted(truncatable_primes, reverse=True)