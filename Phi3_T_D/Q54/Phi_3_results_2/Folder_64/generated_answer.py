def all_right_truncatable_prime(tup):
    x = tup[4]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        return all((is_prime(n) for n in ((n := (n // 10 if n % 10 != 0 else 0)) for _ in range(len(str(n))))))
    return sorted((n for n in range(2, x) if is_right_truncatable_prime(n)))