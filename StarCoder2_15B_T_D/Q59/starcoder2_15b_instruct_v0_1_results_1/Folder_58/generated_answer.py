def all_left_truncatable_prime(t):
    x = t[975]

    def is_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if not is_truncatable_prime(n):
            return False
        while n >= 10:
            n //= 10
            if not is_truncatable_prime(n):
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)