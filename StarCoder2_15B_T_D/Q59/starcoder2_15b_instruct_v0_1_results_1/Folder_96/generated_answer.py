def all_left_truncatable_prime(args):
    x = args[29]

    def is_truncatable_prime(n):
        if n < 2 or (n % 2 == 0 and n != 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = [n for n in range(2, x) if is_truncatable_prime(n)]
    left_truncatable_primes.sort()
    return left_truncatable_primes