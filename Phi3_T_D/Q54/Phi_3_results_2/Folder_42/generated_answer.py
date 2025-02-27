def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, digits):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_primes(numbers):
    n = numbers[64]
    truncatable_primes = []
    for i in range(2, n):
        if is_right_truncatable_prime(i, list(str(i))):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)