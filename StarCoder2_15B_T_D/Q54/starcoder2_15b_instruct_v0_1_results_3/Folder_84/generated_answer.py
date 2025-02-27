def all_right_truncatable_prime(tup):
    x = tup[630]

    def is_right_truncatable_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    truncatable_primes = [p for p in range(x) if is_right_truncatable_prime(p)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes