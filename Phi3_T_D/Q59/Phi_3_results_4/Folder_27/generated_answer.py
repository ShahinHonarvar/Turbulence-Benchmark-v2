def all_left_truncatable_prime(values):
    x = values[79]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    truncatable_primes = [i for i in range(2, x) if is_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)