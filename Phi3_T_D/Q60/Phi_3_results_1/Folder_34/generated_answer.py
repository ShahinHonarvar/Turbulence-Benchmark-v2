def all_left_right_truncatable_prime(prime_tuple):
    x = prime_tuple[18]
    truncatable_primes = []

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
    for prime in range(x, 1, -1):
        if is_prime(prime) and is_truncatable_prime(prime):
            truncatable_primes.append(prime)
    return truncatable_primes