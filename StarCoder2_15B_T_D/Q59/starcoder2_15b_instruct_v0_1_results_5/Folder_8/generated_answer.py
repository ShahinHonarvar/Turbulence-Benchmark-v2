def all_left_truncatable_prime(t):
    x = t[41]

    def is_left_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    return sorted(filter(is_left_truncatable_prime, range(2, x)), reverse=True)