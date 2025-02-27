def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        while s:
            if not is_prime(int(s)) or '0' in s:
                return False
            s = s[1:]
        return True
    x = tup[10]
    primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(primes, reverse=True)