def all_right_truncatable_prime(numbers):
    x = numbers[98]

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        p = 3
        while p * p <= n:
            if n % p == 0:
                return False
            p += 2
        return True

    def is_right_truncatable(n):
        if not is_prime(n):
            return False
        n_str = str(n)
        while n_str:
            if not is_prime(int(n_str)):
                return False
            n_str = n_str[:-1]
        return True
    return sorted([n for n in range(2, x) if is_right_truncatable(n)])