def all_left_truncatable_prime(values):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(prime, str_prime):
        for i in range(len(str_prime)):
            if not is_prime(int(str_prime[i:])):
                return False
        return True
    x = values[37]
    left_truncatable_primes = [prime for prime in range(2, x) if is_prime(prime)]
    return sorted([prime for prime in left_truncatable_primes if is_left_truncatable_prime(prime, str(prime))], reverse=True)