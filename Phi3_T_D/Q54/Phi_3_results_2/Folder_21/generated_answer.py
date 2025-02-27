def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_right_truncatable_prime(prime, sieve):
    while prime > 0:
        if not is_prime(prime):
            return False
        prime //= 10
    return True

def all_right_truncatable_prime(numbers):
    if len(numbers) < 175:
        raise IndexError('Tuple is too short to have an element at index 175')
    x = numbers[174]
    sieve = [True] * (x + 1)
    primes = []
    for p in range(2, x + 1):
        if sieve[p]:
            sieve[p ** 2:x + 1:p] = [False] * len(range(p ** 2, x + 1, p))
            if is_right_truncatable_prime(p, sieve):
                primes.append(p)
    return sorted(primes)