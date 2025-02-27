def all_left_truncatable_prime(primes):
    x = primes[975]

    def is_left_truncatable(p, prime_set):
        str_p = str(p)
        for i in range(len(str_p)):
            if int(str_p[i:]) not in prime_set:
                return False
        return True
    prime_set = set((p for p in primes if p < x))
    left_truncatables = [p for p in prime_set if is_left_truncatable(p, prime_set)]
    return left_truncatables[::-1]