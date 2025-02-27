def all_left_truncatable_prime(t):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        return True
    x = t[65]
    primes = [n for n in range(2, x) if is_prime(n)]
    left_truncatable_primes = [n for n in primes if is_left_truncatable_prime(n) and '0' not in str(n)]
    return sorted(left_truncatable_primes, reverse=True)