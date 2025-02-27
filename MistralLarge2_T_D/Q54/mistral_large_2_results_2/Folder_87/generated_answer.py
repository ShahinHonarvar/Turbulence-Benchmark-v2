def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def right_truncatable_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    right_truncatable = []
    for prime in primes:
        temp = prime
        while temp > 0:
            if not is_prime(temp):
                break
            temp //= 10
        else:
            right_truncatable.append(prime)
    return right_truncatable

def all_right_truncatable_prime(tup):
    x = tup[39]
    primes = right_truncatable_primes(x)
    return sorted(primes, reverse=True)