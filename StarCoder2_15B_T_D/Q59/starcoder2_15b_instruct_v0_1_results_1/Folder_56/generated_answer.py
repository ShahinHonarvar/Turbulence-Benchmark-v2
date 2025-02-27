def all_left_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    left_truncatable_primes = []
    for i in range(10, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    return left_truncatable_primes