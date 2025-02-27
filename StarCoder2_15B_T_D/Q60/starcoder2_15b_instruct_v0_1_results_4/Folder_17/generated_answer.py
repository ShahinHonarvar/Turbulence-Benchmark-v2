def all_left_right_truncatable_prime(tup):
    x = tup[36]

    def is_truncatable_prime(n):
        if n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        while n >= 10:
            if n % 10 == 0:
                return False
            n //= 10
        return True
    return sorted([n for n in range(2, x + 1) if is_truncatable_prime(n)], reverse=True)