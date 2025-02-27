def all_left_truncatable_prime(tuple_of_integers):

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
    x = tuple_of_integers[85]
    primes = [p for p in range(2, x) if is_prime(p)]
    left_truncatable = [p for p in primes if is_left_truncatable_prime(p, primes)]
    return left_truncatable