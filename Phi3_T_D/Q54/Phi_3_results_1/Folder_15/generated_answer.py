def all_right_truncatable_prime(nums_tuple):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n, primality):
        while n > 0:
            if not (is_prime(n) and n in primality):
                return False
            n //= 10
        return True
    x = nums_tuple[6]
    primality = set(range(2, x))
    for i in range(2, int(x ** 0.5) + 1):
        if i in primality:
            primality.difference_update(range(i * 2, x, i))
    right_truncatables = [p for p in primality if is_right_truncatable(p, primality)]
    return sorted(right_truncatables, reverse=True)