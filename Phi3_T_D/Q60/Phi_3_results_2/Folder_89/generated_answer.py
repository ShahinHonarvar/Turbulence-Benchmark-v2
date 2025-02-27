def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    x = x_tuple[97]
    truncatable_primes = [p for p in range(2, x + 1) if is_prime(p) and is_truncatable_prime(p)]
    return sorted(truncatable_primes, reverse=True)