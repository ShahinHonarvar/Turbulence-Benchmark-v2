def all_left_right_truncatable_prime(num_tuple):
    X = num_tuple[41]
    truncatable_primes = []
    primes = [2, 3, 5, 7]

    def is_prime(n):
        for prime in primes:
            if prime * prime > n:
                break
            if n % prime == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    for prime in range(11, X + 1):
        if is_prime(prime) and is_truncatable(prime):
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)