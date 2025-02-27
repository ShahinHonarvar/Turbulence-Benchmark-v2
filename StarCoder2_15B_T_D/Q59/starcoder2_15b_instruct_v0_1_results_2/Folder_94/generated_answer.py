def all_left_truncatable_prime(args):
    x = args[43]

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0 or not is_prime(n):
            return False
        return is_left_truncatable_prime(n // 10)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(x)))