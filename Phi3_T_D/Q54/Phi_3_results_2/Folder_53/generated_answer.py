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

def is_right_truncatable_prime(n, digits):
    prime_so_far = False
    while n > 0:
        if not is_prime(n):
            return False
        prime_so_far = True
        n = n // 10
    return prime_so_far

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n, len(str(n))):
            primes.append(n)
    return sorted(primes, reverse=True)