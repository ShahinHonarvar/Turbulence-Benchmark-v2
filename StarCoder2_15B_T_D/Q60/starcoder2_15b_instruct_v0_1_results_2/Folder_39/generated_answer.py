def all_left_right_truncatable_prime(t):
    x = t[30]

    def is_truncatable_prime(n):
        if n < 10:
            return n in (2, 3, 5, 7)
        return is_truncatable_prime(n % 10) and is_truncatable_prime(n // 10)
    return sorted(filter(is_truncatable_prime, range(x + 1)), reverse=True)