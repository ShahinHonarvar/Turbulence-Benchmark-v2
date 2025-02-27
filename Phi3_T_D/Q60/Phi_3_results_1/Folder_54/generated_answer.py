def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n, _primes):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    x = numbers[88]
    truncatable_primes = [p for p in range(2, x + 1) if p in primes or (is_prime(p) and is_truncatable(p, primes))]
    return sorted(truncatable_primes, reverse=True)