def all_left_truncatable_prime(tuple_of_ints):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable_prime(n, primes_set):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    x = tuple_of_ints[8]
    primes = [p for p in range(x) if is_prime(p)]
    left_truncatables = [p for p in primes if left_truncatable_prime(p, set(primes))]
    return sorted(left_truncatables, reverse=True)