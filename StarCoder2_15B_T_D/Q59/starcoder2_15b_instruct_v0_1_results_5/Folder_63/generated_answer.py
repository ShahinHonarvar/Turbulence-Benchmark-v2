def all_left_truncatable_prime(t):
    x = t[0]

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

    def is_left_truncatable_prime(n):
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if n == 0:
                return True
            if not is_prime(n):
                return False
        return True
    result = []
    for i in range(1, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result