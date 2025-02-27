def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    if not n or n % 2 == 0 or n == 1:
        return False
    while n > 0:
        if not is_prime(n):
            return False
        primes.add(n)
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[433]
    left_truncatable_primes = set()
    for num in range(2, x):
        if is_left_truncatable_prime(num, left_truncatable_primes):
            pass
    return sorted(list(left_truncatable_primes), reverse=True)