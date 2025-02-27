def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, primes):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(numbers):
    primes = [n for n in numbers if is_prime(n)]
    x = numbers[784]
    left_truncatables = [p for p in primes if is_left_truncatable_prime(p, primes)]
    return sorted(left_truncatables)