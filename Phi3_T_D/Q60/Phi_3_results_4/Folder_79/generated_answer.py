def all_left_right_truncatable_prime(primes_tuple):

    def is_truncatable_prime(n, primes_set):
        str_n = str(n)
        length = len(str_n)
        for i in range(length):
            if int(str_n[i:]) not in primes_set or int(str_n[:i + 1]) not in primes_set:
                return False
        return True
    x = primes_tuple[90]
    prime_numbers = {prime for prime in range(2, x + 1) if all((prime % d != 0 for d in range(2, int(prime ** 0.5) + 1)))}
    truncatable_primes = [prime for prime in prime_numbers if is_truncatable_prime(prime, prime_numbers)]
    return sorted(truncatable_primes)