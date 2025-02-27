def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate_left(n):
    n = list(str(n))
    while len(n) > 1:
        n.pop(0)
        yield int(''.join(n))
        if not is_prime(int(''.join(n))):
            return

def all_left_truncatable_prime(numbers):
    x = numbers[11]
    primes = [p for p in range(2, x) if is_prime(p)]
    left_truncatable = []
    for prime in primes:
        left_trunc = list(truncate_left(prime))
        if left_trunc:
            left_truncatable.append(prime)
    return sorted(left_truncatable)