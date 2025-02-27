def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n, base=10):
    while n > 0:
        if not is_prime(n):
            return False
        n //= base
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[177]
    primes = [i for i in range(2, x) if is_prime(i) and is_left_truncatable_prime(i)]
    return primes