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

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[61]
    primes = [2, 3, 5, 7]
    for i in range(11, x, 2):
        if is_prime(i):
            primes.append(i)
    left_truncatable_primes = [p for p in primes if is_left_truncatable_prime(p, primes)]
    return left_truncatable_primes