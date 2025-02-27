def all_left_truncatable_prime(tup):
    x = tup[32]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, original=None):
        if n < original or not is_prime(n):
            return False
        if n < x:
            return True
        return is_left_truncatable_prime(n // 10, original)
    primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num, num):
            primes.append(num)
    return primes