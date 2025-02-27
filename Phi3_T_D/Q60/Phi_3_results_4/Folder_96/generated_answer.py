def all_left_right_truncatable_prime(range_tuple):
    limit = range_tuple[29]
    left_right_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n = str(n)
        if len(n) == 1:
            return is_prime(n)
        for i in range(1, len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:i + 1])):
                return False
        return True
    for n in range(11, limit + 1):
        if is_truncatable(n):
            left_right_primes.append(n)
    return left_right_primes