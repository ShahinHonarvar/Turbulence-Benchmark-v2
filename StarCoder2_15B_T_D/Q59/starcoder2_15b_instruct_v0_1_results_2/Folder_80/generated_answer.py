def all_left_truncatable_prime(t):
    x = t[14]

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if n % 10 == 0:
            return False
        return is_left_truncatable_prime(n // 10) and is_prime(n)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)