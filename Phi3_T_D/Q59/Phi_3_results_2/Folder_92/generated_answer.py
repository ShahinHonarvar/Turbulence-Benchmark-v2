def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if not is_prime(n):
            return False
        while n > 0:
            n = int(str(n)[1:])
            if not is_prime(n):
                return False
        return True
    primes = [i for i in range(2, t[7]) if is_prime(i)]
    left_truncatable_primes = [p for p in primes if is_left_truncatable(p)]
    return left_truncatable_primes