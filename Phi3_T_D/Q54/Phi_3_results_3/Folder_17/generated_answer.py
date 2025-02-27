def all_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n, primes):
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    def get_primes(n):
        primes_sieve = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if primes_sieve[p]:
                for i in range(p * p, n + 1, p):
                    primes_sieve[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes_sieve[p]]
    x = num_tuple[36]
    prime_list = get_primes(x)
    right_truncatable_primes = [p for p in prime_list if is_right_truncatable_prime(p, prime_list)]
    return sorted(right_truncatable_primes, reverse=True)