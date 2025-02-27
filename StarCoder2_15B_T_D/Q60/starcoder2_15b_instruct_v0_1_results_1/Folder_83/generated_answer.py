def all_left_right_truncatable_prime(tup):
    x = tup[24]
    truncatable_primes = []

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        if not is_prime(n):
            return False
        return is_truncatable_prime(n // 10)
    for i in range(2, x + 1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True