def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    if not is_prime(n):
        return False
    while n > 0:
        if n % 10 == 0 or not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(tup):
    x = tup[96]
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)