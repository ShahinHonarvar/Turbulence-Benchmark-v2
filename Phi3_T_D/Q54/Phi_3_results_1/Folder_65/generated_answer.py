def is_right_truncatable_prime(n, primes):
    while n > 0:
        if n not in primes:
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) != 32:
        raise ValueError('Function argument must be a tuple of 32 positive integers.')
    x = numbers[32]
    primes = [2]
    for n in range(3, x, 2):
        if all((n % p != 0 for p in primes)):
            primes.append(n)
    right_truncatable_primes = []
    for p in primes:
        if p < x and is_right_truncatable_prime(p, primes):
            right_truncatable_primes.append(p)
    return sorted(right_truncatable_primes)