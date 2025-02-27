def all_left_right_truncatable_prime(number_range):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, all_primes):
        if n not in all_primes:
            return False
        string_n = str(n)
        if len(string_n) == 1:
            return True
        return is_truncatable_prime(int(string_n[1:]), all_primes) and is_truncatable_prime(int(string_n[:-1]), all_primes)
    limit = number_range[49]
    if limit < 11:
        return []
    all_primes = {i for i in range(2, limit + 1) if is_prime(i)}
    return sorted((x for x in all_primes if is_truncatable_prime(x, all_primes)))