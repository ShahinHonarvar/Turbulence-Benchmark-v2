def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, prime_set):
    while n > 0:
        if not is_prime(n):
            return False
        if n not in prime_set:
            return False
        n = n % 10 ** (len(str(n)) - 1)
    return True

def all_left_right_truncatable_prime(numbers):
    UP_TO = numbers[41]
    primes = [i for i in range(2, UP_TO + 1) if is_prime(i)]
    truncatable_primes = [p for p in primes if len(str(p)) > 1 and is_truncatable(p, set(primes))]
    return sorted(truncatable_primes)