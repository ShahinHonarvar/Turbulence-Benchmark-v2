def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable(n, prime_set):
    if n == 0:
        return False
    if n in prime_set:
        return True
    return is_left_truncatable(n // 10, prime_set)

def all_left_truncatable_prime(integer_tuple):
    x = integer_tuple[88]
    primes_set = set()
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            primes_set.add(i)
            if is_left_truncatable(i, primes_set):
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)