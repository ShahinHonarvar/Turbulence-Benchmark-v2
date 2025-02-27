def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n, primes):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    primes = [i for i in range(2, t[55]) if is_prime(i)]
    result = [p for p in primes if is_left_truncatable_prime(p, primes)]
    return sorted(result, reverse=True)