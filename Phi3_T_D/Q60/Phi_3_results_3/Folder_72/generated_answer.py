def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

def is_truncatable(n, prime_set):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[31]
    primes = set()
    for i in range(2, x + 1):
        if is_prime(i) and is_truncatable(i, primes):
            primes.add(i)
    return sorted(primes, reverse=True)