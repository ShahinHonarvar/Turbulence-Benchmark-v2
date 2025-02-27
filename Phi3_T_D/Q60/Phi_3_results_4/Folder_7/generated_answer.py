def all_left_right_truncatable_prime(nums_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n, prime_set):
        str_n = str(n)
        if len(str_n) == 1 or len(str_n) == 2:
            return is_prime(n) and n not in prime_set
        return is_prime(n) and all((str_n[i:] in prime_set and str_n[:i] in prime_set for i in range(1, len(str_n))))
    x = nums_tuple[803]
    primes = set()
    for potential_prime in range(2, x + 1):
        if is_truncatable_prime(potential_prime, primes):
            primes.add(potential_prime)
    return sorted(list(primes))