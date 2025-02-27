def all_left_truncatable_prime(tup):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n, primes):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = tup[86]
    primes = []
    for i in range(10, x, 2):
        if is_prime(i) and is_truncatable_prime(i, primes):
            primes.append(i)
    return sorted(primes, reverse=True)