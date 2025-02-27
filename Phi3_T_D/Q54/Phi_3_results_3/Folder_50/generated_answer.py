def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n, prime_cache):
    if n in prime_cache:
        return True
    if not is_prime(n):
        return False
    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[:i])):
            return False
    prime_cache.add(n)
    return True

def all_right_truncatable_prime(numbers):
    upper_limit = numbers[57]
    right_truncatable_primes = []
    prime_cache = set()
    for i in range(upper_limit, 1, -1):
        if is_right_truncatable_prime(i, prime_cache):
            right_truncatable_primes.append(i)
    return right_truncatable_primes