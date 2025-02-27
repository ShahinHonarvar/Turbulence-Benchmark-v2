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
        if not is_prime(n):
            return False
        if '0' in str(n):
            return False
        n = int(str(n)[1:])
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[35]
    primes = filter(lambda p: is_left_truncatable_prime(p), range(3, x))
    return sorted(primes, reverse=True)