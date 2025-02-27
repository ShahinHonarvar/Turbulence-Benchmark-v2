def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, sieve):
    while n > 0:
        if not sieve[n]:
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_truncatable_prime(numbers):
    n = numbers[79]
    sieve = [True for _ in range(2, n)]
    length = len(str(n))
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i - 2]:
            for j in range(i * 2, n, i):
                sieve[j - 2] = False
    return sorted([i for i in range(2, n) if is_left_truncatable_prime(i, sieve)], reverse=True)