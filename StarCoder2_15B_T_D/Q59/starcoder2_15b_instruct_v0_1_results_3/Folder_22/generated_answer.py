def all_left_truncatable_prime(tup):
    x = tup[85]

    def is_truncatable_prime(n):
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
    for i in range(2, x):
        n = i
        while n < x:
            if not is_truncatable_prime(n):
                break
            n //= 10
        else:
            result.append(i)
    return sorted(result)