def all_right_truncatable_prime(t):
    x = t[49]

    def is_right_truncatable_prime(n):
        if n < 10:
            return n in [2, 3, 5, 7]
        return is_right_truncatable_prime(n // 10) and is_prime(n)

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
    result = []
    for i in range(10, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)