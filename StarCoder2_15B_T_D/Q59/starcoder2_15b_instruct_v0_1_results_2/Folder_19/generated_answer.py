def all_left_truncatable_prime(tuple_of_integers):
    x = tuple_of_integers[67]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n >= 1:
            if not is_prime(n):
                return False
            n //= 10
        return True
    left_truncatable_primes = [p for p in range(2, x) if is_left_truncatable_prime(p)]
    return sorted(left_truncatable_primes, reverse=True)