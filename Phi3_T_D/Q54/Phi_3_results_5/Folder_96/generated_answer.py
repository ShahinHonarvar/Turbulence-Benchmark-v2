def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, primes_set):
    if n < 10 or not is_prime(n):
        return False
    while n > 0:
        if n not in primes_set:
            return False
        n = n // 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[29]
    primes = set(filter(is_prime, range(2, x)))
    right_truncatable_primes = [p for p in primes if is_right_truncatable_prime(p, primes)]
    return sorted(right_truncatable_primes)